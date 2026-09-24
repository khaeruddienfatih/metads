"""Wrapper tipis untuk Meta Marketing API (Graph API)."""

from __future__ import annotations

import base64
import json
import time
from typing import Any

import requests


class MetaApiError(RuntimeError):
    pass


class MetaClient:
    def __init__(
        self,
        access_token: str,
        ad_account_id: str,
        api_version: str = "v23.0",
        session: requests.Session | None = None,
    ):
        self.token = access_token
        self.account = ad_account_id if ad_account_id.startswith("act_") else f"act_{ad_account_id}"
        self.base = f"https://graph.facebook.com/{api_version}"
        self.session = session or requests.Session()

    def _request(self, method: str, path: str, data: dict[str, Any] | None = None) -> dict:
        payload = {"access_token": self.token}
        for k, v in (data or {}).items():
            if v is None:
                continue
            payload[k] = json.dumps(v) if isinstance(v, (dict, list, bool)) else v
        url = f"{self.base}/{path}"
        if method == "GET":
            resp = self.session.get(url, params=payload, timeout=120)
        else:
            resp = self.session.post(url, data=payload, timeout=300)
        body = resp.json()
        if "error" in body:
            err = body["error"]
            detail = err.get("error_user_msg") or err.get("message")
            raise MetaApiError(f"{method} {path}: {detail} (code {err.get('code')}/{err.get('error_subcode')})")
        return body

    # --- aset -------------------------------------------------------------
    def upload_image(self, content: bytes, name: str) -> str:
        body = self._request(
            "POST",
            f"{self.account}/adimages",
            {"bytes": base64.b64encode(content).decode(), "name": name},
        )
        return next(iter(body["images"].values()))["hash"]

    def upload_video(self, file_url: str, name: str) -> str:
        return self._request("POST", f"{self.account}/advideos", {"file_url": file_url, "name": name})["id"]

    def wait_video_ready(self, video_id: str, timeout: int = 600, interval: int = 10) -> None:
        deadline = time.time() + timeout
        while time.time() < deadline:
            status = self._request("GET", video_id, {"fields": "status"}).get("status", {})
            state = status.get("video_status")
            if state == "ready":
                return
            if state == "error":
                raise MetaApiError(f"Video {video_id} gagal diproses Meta: {status}")
            time.sleep(interval)
        raise MetaApiError(f"Video {video_id} belum siap setelah {timeout} detik")

    # --- struktur iklan ------------------------------------------------------
    def create_campaign(self, params: dict) -> str:
        return self._request("POST", f"{self.account}/campaigns", params)["id"]

    def create_adset(self, params: dict) -> str:
        return self._request("POST", f"{self.account}/adsets", params)["id"]

    def create_creative(self, params: dict) -> str:
        return self._request("POST", f"{self.account}/adcreatives", params)["id"]

    def create_ad(self, params: dict) -> str:
        return self._request("POST", f"{self.account}/ads", params)["id"]
