"""CLI: python -m metads config/campaign.yaml [--apply]"""

from __future__ import annotations

import argparse
import logging
import os
import sys

from .builder import ConfigError, State, load_config, run
from .cloudinary_client import CloudinaryClient
from .meta_client import MetaApiError, MetaClient


def _load_dotenv(path: str = ".env") -> None:
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def _env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        sys.exit(f"Environment variable {name} belum diisi (lihat .env.example)")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Buat iklan Meta (PAUSED) otomatis dari aset Cloudinary.")
    parser.add_argument("config", help="Path file YAML campaign")
    parser.add_argument("--apply", action="store_true", help="Benar-benar buat di Meta (default: dry-run)")
    parser.add_argument("--state-dir", default="state", help="Folder penyimpanan state (default: state/)")
    parser.add_argument("--no-wait-video", action="store_true", help="Jangan tunggu video selesai diproses Meta")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    _load_dotenv()

    try:
        cfg = load_config(args.config)
    except FileNotFoundError:
        sys.exit(f"File config tidak ditemukan: {args.config}")
    except ConfigError as e:
        sys.exit(f"Config tidak valid: {e}")

    cloudinary = CloudinaryClient(
        _env("CLOUDINARY_CLOUD_NAME"), _env("CLOUDINARY_API_KEY"), _env("CLOUDINARY_API_SECRET")
    )
    meta = None
    if args.apply:
        meta = MetaClient(
            _env("META_ACCESS_TOKEN"),
            _env("META_AD_ACCOUNT_ID"),
            os.environ.get("META_API_VERSION", "v23.0"),
        )

    state = State.load(args.state_dir, cfg["name"])
    try:
        result = run(cfg, cloudinary, meta, state, apply=args.apply, wait_video=not args.no_wait_video)
    except MetaApiError as e:
        print(f"\nGAGAL: {e}\nObjek yang sudah dibuat tersimpan di {state.path}; jalankan ulang untuk melanjutkan.")
        return 1

    if args.apply:
        print(f"\nSelesai: {len(result.created)} objek dibuat (semua PAUSED). State: {state.path}")
    else:
        print(f"\nDRY-RUN: {len(result.planned)} objek akan dibuat. Tambahkan --apply untuk menjalankan.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
