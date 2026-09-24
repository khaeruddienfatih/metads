"""Membuat halaman HTML berisi mockup iklan (gaya feed Facebook) sebelum dibuat di Meta."""

from __future__ import annotations

import html
from urllib.parse import urlparse

from .builder import ad_name
from .cloudinary_client import Asset

CTA_LABELS = {
    "LEARN_MORE": "Selengkapnya",
    "SHOP_NOW": "Belanja Sekarang",
    "SIGN_UP": "Daftar",
    "CONTACT_US": "Hubungi Kami",
    "WHATSAPP_MESSAGE": "Kirim Pesan WhatsApp",
    "BOOK_TRAVEL": "Pesan Sekarang",
    "GET_QUOTE": "Dapatkan Penawaran",
    "APPLY_NOW": "Daftar Sekarang",
}

MAX_ADS_PER_ADSET = 50


def media_url(asset: Asset, width: int) -> str:
    """URL Cloudinary yang sudah di-crop 4:5 seperti tampilan feed."""
    t = f"w_{width},c_fill,ar_4:5,g_auto,q_auto"
    if asset.is_video:
        return f"https://res.cloudinary.com/{asset.cloud_name}/video/upload/so_0,{t}/{asset.public_id}.jpg"
    return f"https://res.cloudinary.com/{asset.cloud_name}/image/upload/{t},f_auto/{asset.public_id}"


def _rupiah(amount) -> str:
    return f"Rp{int(amount):,}".replace(",", ".") if amount else "-"


def _e(text) -> str:
    return html.escape(str(text or ""))


def _feed_card(cfg: dict, adset: dict, copy: dict, asset: Asset | None, label: str) -> str:
    text = copy["primary_text"].strip()
    lines = text.split("\n")
    teaser, rest = "\n".join(lines[:3]), "\n".join(lines[3:])
    domain = "WHATSAPP" if adset.get("destination") == "whatsapp" else urlparse(adset["link"]).netloc.removeprefix("www.").upper()
    cta = CTA_LABELS.get(adset.get("call_to_action", "LEARN_MORE"), adset.get("call_to_action", ""))
    page = cfg.get("page_name", "Elharamain Wisata")
    initials = "".join(w[0] for w in page.split()[:2]).upper()
    if asset:
        media = (
            f'<div class="media"><img src="{_e(media_url(asset, 640))}" alt="" title="{_e(asset.short_name)}" loading="lazy">'
            + ('<span class="play" aria-label="video">▶</span>' if asset.is_video else "")
            + "</div>"
        )
    else:
        media = '<div class="media empty">Belum ada creative di folder ini</div>'
    more = (
        f'<details><summary>… Lihat selengkapnya</summary><div class="rest">{_e(rest)}</div></details>'
        if rest.strip()
        else ""
    )
    desc = f'<div class="desc">{_e(copy.get("description"))}</div>' if copy.get("description") else ""
    return f"""
<figure class="variant">
  <figcaption>{_e(label)}</figcaption>
  <article class="post">
    <header class="post-head">
      <span class="avatar">{_e(initials)}</span>
      <span><b>{_e(page)}</b><small>Bersponsor · 🌐</small></span>
    </header>
    <div class="body">{_e(teaser)}{more}</div>
    {media}
    <footer class="linkbar">
      <div class="linktext">
        <small>{_e(domain)}</small>
        <b class="headline">{_e(copy["headline"])}</b>
        {desc}
      </div>
      <span class="cta">{_e(cta)}</span>
    </footer>
  </article>
</figure>"""


def _campaign_section(cfg: dict, assets_by_adset: dict[str, list[Asset]]) -> str:
    c = cfg["campaign"]
    parts = []
    for adset in cfg["adsets"]:
        assets = assets_by_adset.get(adset["name"], [])
        copies = adset["copies"]
        total = min(len(assets) * len(copies), MAX_ADS_PER_ADSET)
        budget = adset.get("daily_budget") or c.get("daily_budget")
        n_img = sum(not a.is_video for a in assets)
        n_vid = len(assets) - n_img
        cards = "".join(
            _feed_card(cfg, adset, copy, assets[0] if assets else None, f"Judul {i + 1}")
            for i, copy in enumerate(copies)
        )
        thumbs = "".join(
            f'<li><div class="thumb"><img src="{_e(media_url(a, 240))}" alt="" loading="lazy">'
            + ('<span class="play sm">▶</span>' if a.is_video else "")
            + f'</div><code>{_e(a.short_name)}</code>'
            + "".join(f"<small>{_e(ad_name(adset, a, j))}</small>" for j in range(len(copies)))
            + "</li>"
            for a in assets
        )
        parts.append(f"""
<div class="adset">
  <dl class="facts">
    <div><dt>Ad set</dt><dd>{_e(adset["name"])}</dd></div>
    <div><dt>Folder Cloudinary</dt><dd><code>{_e(adset["source"].get("folder") or adset["source"].get("tag"))}</code></dd></div>
    <div><dt>Creative</dt><dd>{n_img} gambar · {n_vid} video</dd></div>
    <div><dt>Iklan dibuat</dt><dd class="num">{len(assets)} × {len(copies)} judul = {total}</dd></div>
    <div><dt>Budget harian</dt><dd class="num">{_rupiah(budget)}</dd></div>
  </dl>
  <div class="variants">{cards}</div>
  <details class="all"><summary>Lihat semua {len(assets)} creative</summary><ul class="grid">{thumbs}</ul></details>
</div>""")
    return f"""
<section class="campaign" id="{_e(cfg["name"])}">
  <h2>{_e(c["name"])} <span class="pill">PAUSED</span></h2>
  <p class="meta">Tujuan: <b>{_e(c["objective"])}</b> · Link: {_e(cfg["adsets"][0]["link"])}</p>
  {"".join(parts)}
</section>"""


CSS = """
:root{--bg:#f0f2f5;--card:#fff;--ink:#1c1e21;--muted:#65676b;--line:#dadde1;--link:#f0f2f5;--accent:#1b6b4f;--accent-ink:#fff;--pill:#fff4d6;--pill-ink:#7a5a00}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#18191a;--card:#242526;--ink:#e4e6eb;--muted:#b0b3b8;--line:#3a3b3c;--link:#3a3b3c;--accent:#4fb58c;--accent-ink:#0d1f18;--pill:#4a3b10;--pill-ink:#ffd978;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#18191a;--card:#242526;--ink:#e4e6eb;--muted:#b0b3b8;--line:#3a3b3c;--link:#3a3b3c;--accent:#4fb58c;--accent-ink:#0d1f18;--pill:#4a3b10;--pill-ink:#ffd978;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 "Segoe UI",Helvetica,Arial,sans-serif;padding-inline:16px;padding-block:24px 64px}
main{max-width:1040px;margin:0 auto}
h1{font-size:26px;margin:0 0 4px;text-wrap:balance}
.lead{color:var(--muted);margin:0 0 16px;max-width:65ch}
nav{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px}
nav a{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 14px;color:var(--ink);text-decoration:none;font-weight:600;font-size:14px}
nav a:hover,nav a:focus-visible{border-color:var(--accent);outline:none}
.campaign{border-top:1px solid var(--line);padding-top:24px;margin-top:32px}
h2{font-size:20px;margin:0;display:flex;flex-wrap:wrap;align-items:center;gap:10px;text-wrap:balance}
.pill{background:var(--pill);color:var(--pill-ink);font-size:11px;letter-spacing:.06em;padding:3px 8px;border-radius:4px}
.meta{color:var(--muted);margin:6px 0 16px;overflow-wrap:anywhere}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:0 0 20px}
.facts div{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px}
dt{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
dd{margin:2px 0 0;font-weight:600;overflow-wrap:anywhere}
.num{font-variant-numeric:tabular-nums}
.variants{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;align-items:start}
.variant{margin:0}
figcaption{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);margin-bottom:6px}
.post{background:var(--card);border-radius:10px;box-shadow:0 1px 2px rgba(0,0,0,.2);overflow:hidden;max-width:500px}
.post-head{display:flex;gap:10px;align-items:center;padding:12px 16px 8px}
.post-head b{display:block;font-size:15px}
.post-head small{color:var(--muted);font-size:13px}
.avatar{width:40px;height:40px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;font-weight:700;flex:none}
.body{padding:0 16px 12px;white-space:pre-line}
.body details summary{color:var(--muted);font-weight:600;cursor:pointer;list-style:none;margin-top:2px}
.body details summary::-webkit-details-marker{display:none}
.body details[open] summary{display:none}
.media{position:relative;aspect-ratio:4/5;background:var(--link);max-width:100%}
.media img{width:100%;height:100%;object-fit:cover;display:block}
.media.empty{display:grid;place-items:center;color:var(--muted)}
.play{position:absolute;inset:50% auto auto 50%;transform:translate(-50%,-50%);width:56px;height:56px;border-radius:50%;background:rgba(0,0,0,.55);color:#fff;display:grid;place-items:center;font-size:22px;padding-left:4px}
.play.sm{width:30px;height:30px;font-size:12px;padding-left:2px}
.linkbar{display:flex;gap:12px;align-items:center;justify-content:space-between;background:var(--link);padding:10px 16px}
.linktext{min-width:0}
.linktext small{display:block;color:var(--muted);font-size:12px}
.headline{display:block;font-size:16px;line-height:1.25;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.desc{color:var(--muted);font-size:13px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cta{flex:none;background:var(--line);color:var(--ink);font-weight:600;font-size:14px;padding:8px 12px;border-radius:6px}
.all{margin-top:20px}
.all>summary{cursor:pointer;font-weight:600;color:var(--accent)}
.grid{list-style:none;padding:0;margin:12px 0 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px}
.grid li{display:flex;flex-direction:column;gap:3px;min-width:0}
.thumb{position:relative;aspect-ratio:4/5;border-radius:6px;overflow:hidden;background:var(--link)}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
.grid code{font-size:12px;overflow-wrap:anywhere}
.grid small{color:var(--muted);font-size:11px;overflow-wrap:anywhere}
.adset+.adset{margin-top:28px}
"""


def render(campaigns: list[tuple[dict, dict[str, list[Asset]]]]) -> str:
    nav = "".join(f'<a href="#{_e(cfg["name"])}">{_e(cfg["campaign"]["name"].replace("[AUTO] ", ""))}</a>'
                  for cfg, _ in campaigns)
    total = sum(
        min(len(assets.get(a["name"], [])) * len(a["copies"]), MAX_ADS_PER_ADSET)
        for cfg, assets in campaigns
        for a in cfg["adsets"]
    )
    sections = "".join(_campaign_section(cfg, assets) for cfg, assets in campaigns)
    return f"""<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Preview Iklan</title>
<style>{CSS}</style></head><body>
<main>
  <h1>Preview Iklan</h1>
  <p class="lead">{len(campaigns)} campaign, {total} iklan. Belum ada yang dibuat di Meta: semua iklan akan dibuat
  dengan status PAUSED saat script dijalankan dengan <code>--apply</code>. Setiap creative dibuat
  satu iklan per judul supaya judul bisa di-test.</p>
  <nav>{nav}</nav>
  {sections}
</main></body></html>"""


def main(argv: list[str] | None = None) -> int:
    import argparse
    import os
    from pathlib import Path

    from .builder import load_config
    from .cli import _env, _load_dotenv
    from .cloudinary_client import CloudinaryClient

    parser = argparse.ArgumentParser(description="Buat preview HTML iklan dari config + aset Cloudinary.")
    parser.add_argument("configs", nargs="+", help="Satu atau lebih file YAML campaign")
    parser.add_argument("-o", "--output", default="preview.html", help="File HTML hasil (default: preview.html)")
    args = parser.parse_args(argv)

    _load_dotenv()
    cloudinary = CloudinaryClient(
        _env("CLOUDINARY_CLOUD_NAME"), _env("CLOUDINARY_API_KEY"), _env("CLOUDINARY_API_SECRET")
    )
    campaigns = []
    for path in args.configs:
        cfg = load_config(path)
        assets = {
            a["name"]: cloudinary.search(
                folder=a["source"].get("folder"), tag=a["source"].get("tag"), max_results=a["source"].get("max_assets", 50)
            )
            for a in cfg["adsets"]
        }
        campaigns.append((cfg, assets))
    Path(args.output).write_text(render(campaigns), encoding="utf-8")
    print(f"Preview ditulis ke {os.path.abspath(args.output)} — buka di browser.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
