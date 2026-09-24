"""Membangun Campaign -> Ad Set -> Creative -> Ad dari config YAML + aset Cloudinary.

Semua objek dibuat dengan status PAUSED. State disimpan per config sehingga
menjalankan ulang hanya membuat iklan untuk aset/copy yang belum pernah dibuat.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .cloudinary_client import Asset, CloudinaryClient
from .meta_client import MetaClient

log = logging.getLogger("metads")

STATUS = "PAUSED"
MAX_ADS_PER_ADSET = 50


class ConfigError(ValueError):
    pass


def load_config(path: str | Path) -> dict:
    with open(path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    for adset in cfg.get("adsets") or []:
        adset["copies"] = expand_copies(adset.get("copies") or [])
    validate_config(cfg)
    return cfg


def expand_copies(copies: list[dict]) -> list[dict]:
    """Copy dengan `headlines: [a, b]` dipecah jadi satu varian per headline."""
    out = []
    for copy in copies:
        headlines = copy.get("headlines")
        if not headlines:
            out.append(copy)
            continue
        base = {k: v for k, v in copy.items() if k != "headlines"}
        out.extend({**base, "headline": h} for h in headlines)
    return out


def validate_config(cfg: dict) -> None:
    for key in ("name", "page_id", "campaign", "adsets"):
        if not cfg.get(key):
            raise ConfigError(f"Config wajib punya '{key}'")
    campaign = cfg["campaign"]
    for key in ("name", "objective"):
        if not campaign.get(key):
            raise ConfigError(f"campaign wajib punya '{key}'")
    cbo = bool(campaign.get("daily_budget") or campaign.get("lifetime_budget"))
    names = set()
    for i, adset in enumerate(cfg["adsets"]):
        where = f"adsets[{i}]"
        for key in ("name", "targeting", "optimization_goal", "source", "link", "copies"):
            if not adset.get(key):
                raise ConfigError(f"{where} wajib punya '{key}'")
        if adset["name"] in names:
            raise ConfigError(f"Nama ad set duplikat: {adset['name']}")
        names.add(adset["name"])
        if not cbo and not (adset.get("daily_budget") or adset.get("lifetime_budget")):
            raise ConfigError(f"{where}: isi daily_budget di ad set, atau di campaign (CBO)")
        if not (adset["source"].get("folder") or adset["source"].get("tag")):
            raise ConfigError(f"{where}.source wajib punya 'folder' dan/atau 'tag'")
        for j, copy in enumerate(adset["copies"]):
            if not copy.get("primary_text") or not copy.get("headline"):
                raise ConfigError(f"{where}.copies[{j}] wajib punya 'primary_text' dan 'headline'")


# --- state -------------------------------------------------------------------


@dataclass
class State:
    path: Path
    data: dict = field(default_factory=dict)

    @classmethod
    def load(cls, state_dir: str | Path, name: str) -> "State":
        path = Path(state_dir) / f"{name}.json"
        data = json.loads(path.read_text()) if path.exists() else {}
        data.setdefault("campaign_id", None)
        data.setdefault("media", {})
        data.setdefault("adsets", {})
        return cls(path, data)

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=2, ensure_ascii=False))

    def adset(self, name: str) -> dict:
        return self.data["adsets"].setdefault(name, {"id": None, "ads": {}})


# --- payload builders ----------------------------------------------------------


def campaign_params(cfg: dict) -> dict:
    c = cfg["campaign"]
    params: dict[str, Any] = {
        "name": c["name"],
        "objective": c["objective"],
        "status": STATUS,
        "buying_type": "AUCTION",
        "special_ad_categories": c.get("special_ad_categories", []),
    }
    if c.get("daily_budget") or c.get("lifetime_budget"):
        params["daily_budget"] = c.get("daily_budget")
        params["lifetime_budget"] = c.get("lifetime_budget")
        params["bid_strategy"] = c.get("bid_strategy", "LOWEST_COST_WITHOUT_CAP")
    else:
        # Wajib diisi Meta untuk campaign tanpa CBO.
        params["is_adset_budget_sharing_enabled"] = c.get("adset_budget_sharing", False)
    return params


def adset_params(adset: dict, campaign_id: str, cbo: bool) -> dict:
    params: dict[str, Any] = {
        "name": adset["name"],
        "campaign_id": campaign_id,
        "status": STATUS,
        "targeting": adset["targeting"],
        "optimization_goal": adset["optimization_goal"],
        "billing_event": adset.get("billing_event", "IMPRESSIONS"),
        "promoted_object": adset.get("promoted_object"),
        "start_time": adset.get("start_time"),
        "end_time": adset.get("end_time"),
    }
    if not cbo:
        params["daily_budget"] = adset.get("daily_budget")
        params["lifetime_budget"] = adset.get("lifetime_budget")
        params["bid_strategy"] = adset.get("bid_strategy", "LOWEST_COST_WITHOUT_CAP")
        params["bid_amount"] = adset.get("bid_amount")
    return params


def creative_params(cfg: dict, adset: dict, asset: Asset, media_id: str, copy: dict, name: str) -> dict:
    cta = {"type": adset.get("call_to_action", "LEARN_MORE"), "value": {"link": adset["link"]}}
    spec: dict[str, Any] = {"page_id": str(cfg["page_id"])}
    if cfg.get("instagram_user_id"):
        spec["instagram_user_id"] = str(cfg["instagram_user_id"])
    if asset.is_video:
        spec["video_data"] = {
            "video_id": media_id,
            "image_url": asset.thumbnail_url,
            "message": copy["primary_text"],
            "title": copy["headline"],
            "link_description": copy.get("description"),
            "call_to_action": cta,
        }
    else:
        spec["link_data"] = {
            "image_hash": media_id,
            "link": adset["link"],
            "message": copy["primary_text"],
            "name": copy["headline"],
            "description": copy.get("description"),
            "call_to_action": cta,
        }
    for key in ("video_data", "link_data"):
        if key in spec:
            spec[key] = {k: v for k, v in spec[key].items() if v is not None}
    params: dict[str, Any] = {"name": name, "object_story_spec": spec}
    if adset.get("url_tags"):
        params["url_tags"] = adset["url_tags"]
    return params


def ad_name(adset: dict, asset: Asset, copy_index: int) -> str:
    template = adset.get("ad_name_template", "{adset} | {asset} | copy{copy}")
    return template.format(adset=adset["name"], asset=asset.short_name, copy=copy_index + 1)


# --- runner --------------------------------------------------------------------


@dataclass
class Result:
    planned: list[str] = field(default_factory=list)
    created: list[str] = field(default_factory=list)


def run(
    cfg: dict,
    cloudinary: CloudinaryClient,
    meta: MetaClient | None,
    state: State,
    apply: bool = False,
    wait_video: bool = True,
) -> Result:
    """Dry-run (apply=False) hanya mengisi Result.planned tanpa memanggil Meta."""
    if apply and meta is None:
        raise ValueError("MetaClient diperlukan untuk --apply")
    result = Result()
    cbo = bool(cfg["campaign"].get("daily_budget") or cfg["campaign"].get("lifetime_budget"))

    def step(msg: str) -> None:
        (result.created if apply else result.planned).append(msg)
        log.info("%s %s", "CREATE" if apply else "PLAN  ", msg)

    campaign_id = state.data["campaign_id"]
    if not campaign_id:
        step(f"campaign '{cfg['campaign']['name']}' ({cfg['campaign']['objective']})")
        if apply:
            campaign_id = meta.create_campaign(campaign_params(cfg))
            state.data["campaign_id"] = campaign_id
            state.save()

    for adset in cfg["adsets"]:
        src = adset["source"]
        assets = cloudinary.search(folder=src.get("folder"), tag=src.get("tag"), max_results=src.get("max_assets", 50))
        if not assets:
            log.warning("Tidak ada aset Cloudinary untuk ad set '%s' (%s)", adset["name"], src)
            continue

        ad_state = state.adset(adset["name"])
        pending = [
            (asset, i, copy)
            for asset in assets
            for i, copy in enumerate(adset["copies"])
            if f"{asset.public_id}#{i}" not in ad_state["ads"]
        ]
        room = MAX_ADS_PER_ADSET - len(ad_state["ads"])
        if len(pending) > room:
            log.warning("Ad set '%s': %d iklan baru dipotong jadi %d (batas %d per ad set)",
                        adset["name"], len(pending), max(room, 0), MAX_ADS_PER_ADSET)
            pending = pending[: max(room, 0)]
        if not pending:
            log.info("Ad set '%s': tidak ada aset baru", adset["name"])
            continue

        adset_id = ad_state["id"]
        if not adset_id:
            step(f"  ad set '{adset['name']}'")
            if apply:
                adset_id = meta.create_adset(adset_params(adset, campaign_id, cbo))
                ad_state["id"] = adset_id
                state.save()

        for asset, i, copy in pending:
            name = ad_name(adset, asset, i)
            step(f"    ad '{name}' [{asset.resource_type}: {asset.public_id}]")
            if not apply:
                continue
            media_id = state.data["media"].get(asset.public_id)
            if not media_id:
                if asset.is_video:
                    media_id = meta.upload_video(asset.url, asset.short_name)
                    if wait_video:
                        meta.wait_video_ready(media_id)
                else:
                    media_id = meta.upload_image(cloudinary.download(asset.url), asset.short_name)
                state.data["media"][asset.public_id] = media_id
                state.save()
            creative_id = meta.create_creative(creative_params(cfg, adset, asset, media_id, copy, name))
            ad_id = meta.create_ad(
                {"name": name, "adset_id": adset_id, "creative": {"creative_id": creative_id}, "status": STATUS}
            )
            ad_state["ads"][f"{asset.public_id}#{i}"] = ad_id
            state.save()

    return result
