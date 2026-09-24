from pathlib import Path

import pytest

from metads.builder import ConfigError, State, creative_params, load_config, run, validate_config
from metads.cloudinary_client import Asset

CONFIG = Path(__file__).resolve().parent.parent / "config" / "umroh-premium-1448.yaml"


def make_asset(pid, rtype="image"):
    return Asset(pid, rtype, f"https://res.cloudinary.com/demo/{rtype}/upload/{pid}.jpg", "jpg", "demo")


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


def test_example_config_is_valid():
    cfg = load_config(CONFIG)
    assert "Saudia Airlines" in cfg["adsets"][0]["copies"][0]["primary_text"]


def test_dry_run_does_not_call_meta(tmp_path):
    cfg = load_config(CONFIG)
    result = run(cfg, FakeCloudinary([make_asset("a"), make_asset("b")]), None, State.load(tmp_path, "x"))
    assert len(result.planned) == 4  # campaign + adset + 2 ads
    assert not (tmp_path / "x.json").exists()


def test_apply_creates_everything_paused_and_is_idempotent(tmp_path):
    cfg = load_config(CONFIG)
    meta = FakeMeta()
    cld = FakeCloudinary([make_asset("a"), make_asset("v", "video")])
    run(cfg, cld, meta, State.load(tmp_path, "x"), apply=True)
    assert meta.kinds() == ["campaign", "adset", "image", "creative", "ad", "video", "creative", "ad"]
    for kind, params in meta.calls:
        if kind in ("campaign", "adset", "ad"):
            assert params["status"] == "PAUSED"

    # Jalankan ulang dengan 1 aset baru: hanya aset baru yang dibuat.
    cld.assets.append(make_asset("c"))
    meta2 = FakeMeta()
    run(cfg, cld, meta2, State.load(tmp_path, "x"), apply=True)
    assert meta2.kinds() == ["image", "creative", "ad"]
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
    del cfg["adsets"][0]["daily_budget"]
    with pytest.raises(ConfigError):
        validate_config(cfg)
