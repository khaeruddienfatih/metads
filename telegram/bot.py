#!/usr/bin/env python3
"""Bot Telegram untuk Mac mini Ubuntu — cek & perintah iklan Elharamain lewat Telegram.

Cara kerja: bot membaca pesan Telegram (long polling, tanpa library tambahan), lalu
- perintah cepat (/log, /routine, /git) dijawab langsung dari repo;
- pesan biasa / perintah /laporan diteruskan ke Claude Code headless
  (`claude -p ...`) di folder repo ini, jawabannya dikirim balik ke Telegram.

Hanya chat ID di TELEGRAM_ALLOWED_CHAT_IDS yang dilayani; pesan dari orang lain diabaikan.

Konfigurasi lewat file telegram/.env (TIDAK di-commit, lihat telegram/.env.example):
  TELEGRAM_BOT_TOKEN=...            token dari @BotFather
  TELEGRAM_ALLOWED_CHAT_IDS=12345   chat ID Anda (pisahkan koma kalau lebih dari satu)
  CLAUDE_BIN=claude                 opsional, path ke binary claude
  CLAUDE_TIMEOUT=900                opsional, batas detik per pertanyaan
"""
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENV_FILE = Path(__file__).resolve().parent / ".env"


def load_env():
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


load_env()
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
ALLOWED = {int(x) for x in os.environ.get("TELEGRAM_ALLOWED_CHAT_IDS", "").replace(" ", "").split(",") if x}
CLAUDE = os.environ.get("CLAUDE_BIN", "claude")
TIMEOUT = int(os.environ.get("CLAUDE_TIMEOUT", "900"))
API = f"https://api.telegram.org/bot{TOKEN}"
# Tool yang boleh dipakai Claude saat dijalankan dari Telegram (connector Meta Ads & Gmail akun claude.ai)
ALLOWED_TOOLS = os.environ.get("CLAUDE_ALLOWED_TOOLS",
                               "mcp__claude_ai_meta_ads,mcp__claude_ai_Gmail,Bash,Read,Edit,Write,Glob,Grep")

BANTUAN = """Assalamu'alaikum. Bot iklan Elharamain siap.

Perintah cepat:
/laporan — laporan chat & biaya HARI INI s.d. sekarang (Umroh per akun, Haji per CS)
/kemarin — rekap kemarin
/log — 5 catatan kerja terakhir (chat-log)
/routine — jadwal routine otomatis
/id — tampilkan chat ID Anda

Atau ketik perintah biasa, misalnya:
"cek iklan baru yang belum aktif"
"laporan haji per CS hari ini"
Perintah diteruskan ke Claude (butuh 1–5 menit)."""


def api(method, **params):
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(f"{API}/{method}", data=data, timeout=70) as r:
        return json.loads(r.read().decode())


def kirim(chat_id, teks):
    teks = teks.strip() or "(kosong)"
    for i in range(0, len(teks), 3900):
        try:
            api("sendMessage", chat_id=chat_id, text=teks[i:i + 3900])
        except Exception as e:  # jangan biarkan bot mati karena satu pesan gagal
            print("gagal kirim:", e, file=sys.stderr)


def git_pull():
    subprocess.run(["git", "pull", "-q", "--rebase", "origin", "main"], cwd=REPO,
                   capture_output=True, text=True, timeout=120)


def log_terakhir(n=5):
    git_pull()
    teks = (REPO / "memory" / "chat-log.md").read_text()
    bagian = teks.split("\n### ")
    return "\n\n".join("### " + b.strip() for b in bagian[-n:])


def routine():
    return """Routine otomatis (cloud, jalan walau komputer mati):
• tiap 30 menit (:13 & :43) — nyalakan ad set rule-off CPR < Rp35rb, pause ad set/iklan boros
• 22:00 — semua ad set OFF
• 04:00 — naik anggaran +10% (pemenang 3 hari) lalu ad set ON
• 06:00 — email Rekap Harian ke elharamainwisata
• 08:00 — email Rekap Harian ke pimpinan (dicek otomatis dulu)
• 12:00 / 16:00 / 21:00 — email laporan Siang/Sore/Malam ke elharamainwisata
Detail & ID: memory/chat-memory.md"""


def tanya_claude(chat_id, pertanyaan):
    git_pull()
    prompt = (
        "Pesan ini datang dari user lewat bot Telegram (Mac mini Ubuntu). "
        "Jawab singkat dalam Bahasa Indonesia, cocok dibaca di layar HP (hindari tabel lebar; "
        "pakai daftar pendek). Ikuti CLAUDE.md seperti biasa.\n\nPesan user: " + pertanyaan
    )
    kirim(chat_id, "⏳ Sedang diproses Claude…")
    try:
        api("sendChatAction", chat_id=chat_id, action="typing")
    except Exception:
        pass
    try:
        hasil = subprocess.run([CLAUDE, "-p", prompt, "--output-format", "text",
                                "--allowedTools", ALLOWED_TOOLS], cwd=REPO,
                               capture_output=True, text=True, timeout=TIMEOUT)
        jawab = hasil.stdout.strip() or ("Error:\n" + hasil.stderr.strip()[-3000:])
    except subprocess.TimeoutExpired:
        jawab = f"Waktu habis ({TIMEOUT} detik). Coba perintah yang lebih spesifik."
    kirim(chat_id, jawab)


def proses(msg):
    chat_id = msg["chat"]["id"]
    teks = (msg.get("text") or "").strip()
    if teks == "/id":
        kirim(chat_id, f"Chat ID Anda: {chat_id}")
        return
    if chat_id not in ALLOWED:
        print(f"diabaikan: chat {chat_id} tidak diizinkan", file=sys.stderr)
        return
    if teks in ("/start", "/help", "/bantuan"):
        kirim(chat_id, BANTUAN)
    elif teks == "/log":
        kirim(chat_id, log_terakhir())
    elif teks == "/routine":
        kirim(chat_id, routine())
    elif teks == "/laporan":
        tanya_claude(chat_id, "Buat laporan chat WA & biaya HARI INI s.d. sekarang (read-only): "
                              "ringkasan Umroh/Haji, Umroh per akun, Haji per CS, urut biaya terbesar.")
    elif teks == "/kemarin":
        tanya_claude(chat_id, "Buat rekap chat WA & biaya KEMARIN (read-only, tanggal dari "
                              "tools/tanggal_laporan.py): ringkasan, Umroh per akun, Haji per CS, urut biaya terbesar.")
    elif teks:
        tanya_claude(chat_id, teks)


def main():
    if not TOKEN:
        sys.exit("TELEGRAM_BOT_TOKEN belum diisi di telegram/.env")
    if not ALLOWED:
        print("PERINGATAN: TELEGRAM_ALLOWED_CHAT_IDS kosong — kirim /id ke bot untuk melihat chat ID Anda.",
              file=sys.stderr)
    offset = 0
    print("Bot berjalan…", file=sys.stderr)
    while True:
        try:
            r = api("getUpdates", offset=offset, timeout=60)
            for u in r.get("result", []):
                offset = u["update_id"] + 1
                if "message" in u:
                    proses(u["message"])
        except Exception as e:
            print("error polling:", e, file=sys.stderr)
            time.sleep(5)


if __name__ == "__main__":
    main()
