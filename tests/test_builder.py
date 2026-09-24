from pathlib import Path

import pytest

from metads.builder import ConfigError, State, creative_params, load_config, run, validate_config
from metads.cloudinary_client import Asset

CONFIG = Path(__file__).resolve().parent.parent / "config" / "aini-umroh-1448.yaml"


def one_adset_config():
    """Config AIni dengan hanya ad set pertama, supaya hitungan di test sederhana."""
    cfg = load_config(CONFIG)
    cfg["adsets"] = cfg["adsets"][:1]
    return cfg


def make_asset(pid, rtype="image"):
    ext = "mp4" if rtype == "video" else "jpg"
    return Asset(pid, rtype, f"https://res.cloudinary.com/demo/{rtype}/upload/{pid}.{ext}", ext, "demo")


class FakeCloudinary:
    def __init__(self, assets):
        self.assets = assets

    def search(self, folder=None, tag=None, max_results=50):
        return self.assets[:max_results]

    def download(self, url):
        return b"img"


class FakeMeta:
    def __init__(self):
        self.calls = []
        self.n = 0

    def _id(self, kind, params=None):
        self.n += 1
        self.calls.append((kind, params))
        return f"{kind}_{self.n}"

    def create_campaign(self, p): return self._id("campaign", p)
    def create_adset(self, p): return self._id("adset", p)
    def create_creative(self, p): return self._id("creative", p)
    def create_ad(self, p): return self._id("ad", p)
    def upload_image(self, content, name): return self._id("image")
    def upload_video(self, url, name): return self._id("video")
    def wait_video_ready(self, vid): pass

    def kinds(self):
        return [k for k, _ in self.calls]


@pytest.mark.parametrize("adset,text", [
    ("November", "By Riyadh AIr"),
    ("Desember", "Umroh Akhir Tahun Premium By Saudia"),
    ("9 Hari Januari", "Paket Umroh Premium By Saudia"),
    ("12 Hari Januari", "Umroh 12 Hari Premium By Saudia"),
])
def test_aini_config_maps_copy_to_adset(adset, text):
    cfg = load_config(CONFIG)
    a = next(a for a in cfg["adsets"] if a["name"] == adset)
    assert text in a["copies"][0]["primary_text"]
    assert a["source"]["folder"].startswith("Elharamainwisata/Umroh/")


def test_whatsapp_adset_and_creative():
    from metads.builder import adset_params

    cfg = one_adset_config()
    adset = cfg["adsets"][0]
    p = adset_params(adset, "c1", cbo=True, page_id=cfg["page_id"])
    assert p["optimization_goal"] == "CONVERSATIONS"
    assert p["destination_type"] == "WHATSAPP"
    assert p["promoted_object"] == {"page_id": "588336968031663"}
    assert "daily_budget" not in p  # budget di campaign (CBO)
    c = creative_params(cfg, adset, make_asset("a"), "hash", adset["copies"][0], "n")
    ld = c["object_story_spec"]["link_data"]
    assert ld["link"] == "https://api.whatsapp.com/send"
    assert ld["call_to_action"]["type"] == "WHATSAPP_MESSAGE"
    assert ld["call_to_action"]["value"]["app_destination"] == "WHATSAPP"


def test_dry_run_does_not_call_meta(tmp_path):
    cfg = one_adset_config()
    result = run(cfg, FakeCloudinary([make_asset("a"), make_asset("b")]), None, State.load(tmp_path, "x"))
    assert len(result.planned) == 6  # campaign + adset + 2 aset x 2 judul
    assert not (tmp_path / "x.json").exists()


def test_apply_creates_everything_paused_and_is_idempotent(tmp_path):
    cfg = one_adset_config()
    meta = FakeMeta()
    cld = FakeCloudinary([make_asset("a"), make_asset("v", "video")])
    run(cfg, cld, meta, State.load(tmp_path, "x"), apply=True)
    # 2 judul per aset -> 2 iklan per aset, media cukup di-upload sekali.
    assert meta.kinds() == [
        "campaign", "adset",
        "image", "creative", "ad", "creative", "ad",
        "video", "creative", "ad", "creative", "ad",
    ]
    for kind, params in meta.calls:
        if kind in ("campaign", "adset", "ad"):
            assert params["status"] == "PAUSED"

    # Jalankan ulang dengan 1 aset baru: hanya aset baru yang dibuat.
    cld.assets.append(make_asset("c"))
    meta2 = FakeMeta()
    run(cfg, cld, meta2, State.load(tmp_path, "x"), apply=True)
    assert meta2.kinds() == ["image", "creative", "ad", "creative", "ad"]
    assert meta2.calls[-1][1]["adset_id"] == "adset_2"


def test_video_creative_uses_thumbnail():
    cfg = load_config(CONFIG)
    asset = Asset("f/clip", "video", "https://x/clip.mp4", "mp4", "demo")
    p = creative_params(cfg, cfg["adsets"][0], asset, "vid1", cfg["adsets"][0]["copies"][0], "n")
    vd = p["object_story_spec"]["video_data"]
    assert vd["video_id"] == "vid1"
    assert vd["image_url"] == "https://res.cloudinary.com/demo/video/upload/so_0/f/clip.jpg"


def test_missing_budget_rejected():
    cfg = load_config(CONFIG)
    del cfg["campaign"]["daily_budget"]
    with pytest.raises(ConfigError):
        validate_config(cfg)


def test_headlines_expand_into_variants(tmp_path):
    cfg = load_config(CONFIG)
    copies = cfg["adsets"][0]["copies"]
    assert [c["headline"] for c in copies] == [
        "✈️ Tiket Sudah Confirm, Jadwal Pasti",
        "6700+ Google Review ⭐️⭐️⭐️⭐️⭐️ (5.0)",
    ]
    assert copies[0]["primary_text"] == copies[1]["primary_text"]


def test_image_and_video_with_same_public_id_are_separate_ads(tmp_path):
    cfg = one_adset_config()
    meta = FakeMeta()
    cld = FakeCloudinary([make_asset("saudia_9_hari_4"), make_asset("saudia_9_hari_4", "video")])
    run(cfg, cld, meta, State.load(tmp_path, "x"), apply=True)
    assert meta.kinds().count("ad") == 4
    assert meta.kinds().count("image") == 1 and meta.kinds().count("video") == 1
    names = [p["name"] for k, p in meta.calls if k == "ad"]
    assert len(set(names)) == 4


def test_preview_renders_both_headlines_and_counts():
    from metads.preview import render

    cfg = one_adset_config()
    assets = [make_asset("a"), make_asset("a", "video"), make_asset("b")]
    page = render([(cfg, {cfg["adsets"][0]["name"]: assets})])
    assert "1 campaign, 6 iklan" in page
    assert "Tiket Sudah Confirm, Jadwal Pasti" in page and "6700+ Google Review" in page
    assert "/video/upload/so_0," in page
    assert "Rp150.000" in page
