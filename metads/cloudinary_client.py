"""Mengambil daftar aset (gambar/video) dari Cloudinary lewat Search API."""

from __future__ import annotations

from dataclasses import dataclass

import requests


@dataclass(frozen=True)
class Asset:
    public_id: str
    resource_type: str  # "image" | "video"
    url: str
    format: str
    cloud_name: str

    @property
    def is_video(self) -> bool:
        return self.resource_type == "video"

    @property
    def thumbnail_url(self) -> str:
        """Frame pertama video sebagai JPG (wajib untuk creative video di Meta)."""
        if not self.is_video:
            return self.url
        return f"https://res.cloudinary.com/{self.cloud_name}/video/upload/so_0/{self.public_id}.jpg"

    @property
    def short_name(self) -> str:
        return self.public_id.rsplit("/", 1)[-1]


class CloudinaryClient:
    def __init__(self, cloud_name: str, api_key: str, api_secret: str, session: requests.Session | None = None):
        self.cloud_name = cloud_name
        self.auth = (api_key, api_secret)
        self.session = session or requests.Session()

    def search(self, folder: str | None = None, tag: str | None = None, max_results: int = 100) -> list[Asset]:
        # Akun Cloudinary baru memakai "dynamic folders" (field asset_folder),
        # akun lama memakai "fixed folders" (field folder). Coba keduanya.
        assets = self._search(folder, tag, max_results, folder_field="asset_folder")
        if not assets and folder:
            assets = self._search(folder, tag, max_results, folder_field="folder")
        return assets

    def _search(self, folder: str | None, tag: str | None, max_results: int, folder_field: str) -> list[Asset]:
        parts = []
        if folder:
            parts.append(f'{folder_field}="{folder}"')
        if tag:
            parts.append(f'tags="{tag}"')
        if not parts:
            raise ValueError("Sumber Cloudinary wajib punya 'folder' dan/atau 'tag'.")
        parts.append("(resource_type:image OR resource_type:video)")

        assets: list[Asset] = []
        cursor = None
        while True:
            body = {
                "expression": " AND ".join(parts),
                "sort_by": [{"created_at": "asc"}],
                "max_results": min(max_results, 500),
            }
            if cursor:
                body["next_cursor"] = cursor
            resp = self.session.post(
                f"https://api.cloudinary.com/v1_1/{self.cloud_name}/resources/search",
                json=body,
                auth=self.auth,
                timeout=60,
            )
            resp.raise_for_status()
            data = resp.json()
            for r in data.get("resources", []):
                assets.append(
                    Asset(
                        public_id=r["public_id"],
                        resource_type=r["resource_type"],
                        url=r["secure_url"],
                        format=r.get("format", ""),
                        cloud_name=self.cloud_name,
                    )
                )
            cursor = data.get("next_cursor")
            if not cursor or len(assets) >= max_results:
                return assets[:max_results]

    def download(self, url: str) -> bytes:
        resp = self.session.get(url, timeout=120)
        resp.raise_for_status()
        return resp.content
