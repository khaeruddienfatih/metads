#!/usr/bin/env python3
"""Aturan otomatis iklan Meta — jalan REALTIME di Mac mini (tanpa model, langsung Graph API).

Aturan mengikuti memory/routine-tabel.md (no 1–4, 2b). Default = MODE SIMULASI: hanya mencatat
apa yang AKAN diubah, tidak mengubah apa pun. Nyalakan mode aktif dengan META_RULES_LIVE=1 di telegram/.env.

telegram/.env (TIDAK di-commit):
  META_ACCESS_TOKEN=...        token system user dengan izin ads_management + ads_read (jangan dibagikan)
  META_RULES_LIVE=0            0 = simulasi (default), 1 = benar-benar menyalakan/mematikan
  META_RULES_INTERVAL=120      detik antar pengecekan ad set (default 120)
  META_ADS_INTERVAL=600        detik antar pengecekan iklan sepanjang waktu (default 600)
  TELEGRAM_BOT_TOKEN / TELEGRAM_ALLOWED_CHAT_IDS  (sudah ada) — untuk kabar tiap ada perubahan

Jam tenang 22:00–03:59 WIB: tidak jalan (jadwal malam/pagi tetap di routine cloud).
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ENV_FILE = Path(__file__).resolve().parent / ".env"
LOG_FILE = Path(__file__).resolve().parent / "auto_rules.log"
GRAPH = "https://graph.facebook.com/v21.0"
WIB = ZoneInfo("Asia/Jakarta")

# 14 akun (elharamain Profile 873443374652541 sengaja TIDAK dimasukkan: hasilnya bukan chat WA)
AKUN = {
    "Diana": "1076195694707828", "Tira": "868364731529534", "Nida": "1019832712800468",
    "Hanif": "482252744648260", "Allif": "4678183395742010", "Fikri": "1676215979752437",
    "AIni": "814396810761205", "Irfan": "1060984719243481", "Fifi": "521083143750270",
    "Elharamain Haji": "947788760498911", "Haji 2": "1032468828178224",
    "Haji 3": "794403715776985", "Haji 4": "1526562231314028", "haji": "1050343302646341",
}
CHAT = "onsite_conversion.messaging_conversation_started_7d"

# Angka aturan (samakan dengan memory/routine-tabel.md)
NYALA_ADSET_CPR = 30_000      # no 1: chat>=1 dan CPR hari ini < ini
MATI_ADSET_SPEND = 25_000     # no 2: spend hari ini > ini dan 0 chat
MATI_ADSET_SPEND2 = 45_000    # no 2b: spend hari ini >= ini dan chat < 2
MATI_IKLAN_CPR = 50_000       # no 3: CPR sepanjang waktu > ini
MATI_IKLAN_NOL = 35_000       # 0 chat dan spend >= ini
NYALA_IKLAN_CPR = 30_000      # no 4: CPR sepanjang waktu < ini


def load_env():
    if ENV_FILE.exists():
        for ln in ENV_FILE.read_text().splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and "=" in ln:
                k, v = ln.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


load_env()
TOKEN = os.environ.get("META_ACCESS_TOKEN", "")
LIVE = os.environ.get("META_RULES_LIVE", "0") == "1"
INTERVAL = int(os.environ.get("META_RULES_INTERVAL", "120"))
ADS_EVERY = int(os.environ.get("META_ADS_INTERVAL", "600"))
TG_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TG_CHAT = (os.environ.get("TELEGRAM_ALLOWED_CHAT_IDS", "").replace(" ", "").split(",") or [""])[0]


GAGAL = {}  # (id, status) -> waktu gagal terakhir
PENDING = []  # kabar Telegram dikumpulkan, dikirim satu pesan per putaran


def kirim_pending():
    if PENDING:
        kabari("Aturan otomatis:\n" + "\n".join(PENDING))
        PENDING.clear()


def log(msg):
    baris = f"{datetime.now(WIB):%Y-%m-%d %H:%M:%S} {msg}"
    print(baris, flush=True)
    with LOG_FILE.open("a") as f:
        f.write(baris + "\n")


def kabari(teks):
    if not (TG_TOKEN and TG_CHAT):
        return
    try:
        data = urllib.parse.urlencode({"chat_id": TG_CHAT, "text": teks[:3900]}).encode()
        urllib.request.urlopen(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", data=data, timeout=20)
    except Exception as e:
        print("gagal kirim telegram:", e, file=sys.stderr)


def graph(path, params=None, post=False):
    p = dict(params or {})
    p["access_token"] = TOKEN
    url = f"{GRAPH}/{path}"
    for percobaan in range(3):
        try:
            if post:
                req = urllib.request.Request(url, data=urllib.parse.urlencode(p).encode())
            else:
                req = urllib.request.Request(url + "?" + urllib.parse.urlencode(p))
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            isi = e.read().decode()[:300]
            if e.code in (429, 500, 502, 503) or "request limit" in isi.lower():
                time.sleep(5 * (percobaan + 1))
                continue
            raise RuntimeError(f"HTTP {e.code}: {isi}")
        except urllib.error.URLError:
            time.sleep(3)
    raise RuntimeError("Graph API tidak bisa dihubungi")


def semua(path, params):
    hasil, data = [], graph(path, params)
    while True:
        hasil += data.get("data", [])
        nxt = data.get("paging", {}).get("next")
        if not nxt:
            return hasil
        with urllib.request.urlopen(nxt, timeout=60) as r:
            data = json.loads(r.read().decode())


def angka(item):
    """(spend, chat) dari objek yang punya insights."""
    ins = (item.get("insights") or {}).get("data") or []
    if not ins:
        return 0.0, 0
    spend = float(ins[0].get("spend", 0) or 0)
    chat = sum(int(float(a["value"])) for a in ins[0].get("actions", []) if a["action_type"] == CHAT)
    return spend, chat


def ubah(entity_id, status, label, alasan, sudah):
    if not LIVE:  # simulasi: status tidak berubah, jadi catat sekali saja per hari supaya log tidak banjir
        kunci = (entity_id, status)
        if kunci in sudah:
            return False
        sudah.add(kunci)
    # mode aktif: tanpa batas berapa kali — begitu status berubah, kondisinya tidak cocok lagi
    mode = "AKTIF" if LIVE else "SIMULASI"
    if LIVE:
        if time.time() - GAGAL.get((entity_id, status), 0) < 3600:
            return False  # baru gagal; coba lagi sejam kemudian
        try:
            graph(entity_id, {"status": status}, post=True)
        except RuntimeError as e:  # satu objek bermasalah jangan menghentikan yang lain
            GAGAL[(entity_id, status)] = time.time()
            log(f"GAGAL {label} → {status}: {str(e)[:160]}")
            PENDING.append(f"⚠️ GAGAL {label} → {status}: {str(e)[:120]}")
            return False
    pesan = f"[{mode}] {label} → {status} | {alasan}"
    log(pesan)
    PENDING.append(("✅ " if LIVE else "🧪 ") + pesan)
    return True


def cek_adset(nama, akun, sudah):
    sets = semua(f"act_{akun}/adsets", {
        "fields": "id,name,status,effective_status,optimization_goal,campaign{effective_status},"
                  "insights.date_preset(today){spend,actions}",
        "effective_status": json.dumps(["ACTIVE", "PAUSED"]), "limit": 200})
    for s in sets:
        if s.get("optimization_goal") != "CONVERSATIONS":
            continue
        spend, chat = angka(s)
        cpr = spend / chat if chat else None
        label = f"{nama} · ad set {s['name']} ({s['id']})"
        if s["effective_status"] == "ACTIVE":
            if (spend > MATI_ADSET_SPEND and chat == 0) or (spend >= MATI_ADSET_SPEND2 and chat < 2):
                ubah(s["id"], "PAUSED", label, f"spend hari ini Rp{spend:,.0f}, chat {chat}", sudah)
        elif s["effective_status"] == "PAUSED":
            camp = (s.get("campaign") or {}).get("effective_status")
            if camp == "ACTIVE" and cpr is not None and cpr < NYALA_ADSET_CPR:
                ubah(s["id"], "ACTIVE", label, f"{chat} chat, CPR hari ini Rp{cpr:,.0f}", sudah)


def cek_iklan(nama, akun, sudah):
    iklan = semua(f"act_{akun}/ads", {
        "fields": "id,name,status,effective_status,adset{optimization_goal},"
                  "insights.date_preset(maximum){spend,actions}",
        "effective_status": json.dumps(["ACTIVE", "PAUSED", "ADSET_PAUSED", "CAMPAIGN_PAUSED"]), "limit": 200})
    for a in iklan:
        if (a.get("adset") or {}).get("optimization_goal") != "CONVERSATIONS":
            continue
        spend, chat = angka(a)
        cpr = spend / chat if chat else None
        label = f"{nama} · iklan {a['name']} ({a['id']})"
        if a["status"] == "ACTIVE":
            if (cpr is not None and cpr > MATI_IKLAN_CPR) or (chat == 0 and spend >= MATI_IKLAN_NOL):
                ubah(a["id"], "PAUSED", label, f"sepanjang waktu: {chat} chat, Rp{spend:,.0f}", sudah)
        elif a["status"] == "PAUSED":  # ARCHIVED/DELETED tidak ikut
            if cpr is not None and cpr < NYALA_IKLAN_CPR:
                ubah(a["id"], "ACTIVE", label, f"sepanjang waktu: {chat} chat, CPR Rp{cpr:,.0f}", sudah)


def main():
    if not TOKEN:
        sys.exit("META_ACCESS_TOKEN belum diisi di telegram/.env")
    log(f"mulai — mode {'AKTIF' if LIVE else 'SIMULASI'}, cek ad set tiap {INTERVAL}d, iklan tiap {ADS_EVERY}d")
    sudah, hari, iklan_terakhir = set(), None, 0.0
    while True:
        skrg = datetime.now(WIB)
        if hari != skrg.date():
            sudah.clear()  # hitungan baru tiap hari
            hari = skrg.date()
        if skrg.hour >= 22 or skrg.hour < 4:  # jam tenang
            time.sleep(60)
            continue
        cek_iklan_sekarang = time.time() - iklan_terakhir >= ADS_EVERY
        for nama, akun in AKUN.items():
            try:
                cek_adset(nama, akun, sudah)
                if cek_iklan_sekarang:
                    cek_iklan(nama, akun, sudah)
            except Exception as e:
                log(f"ERROR {nama}: {e}")
        kirim_pending()
        if cek_iklan_sekarang:
            iklan_terakhir = time.time()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
