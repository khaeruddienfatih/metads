# Pindah ke Mac mini Ubuntu + cek lewat Telegram

Disiapkan 2 Nov 2026 atas permintaan user ("saya mau memindahkan ke mac mini ubuntu saya agar bisa saya cek pakai telegram").

## Yang TIDAK perlu dipindah

- **Routine cloud** (cek 30 menit, 22:00 OFF, 04:00 naik anggaran + ON, email 06/08/12/16/21) jalan di cloud
  Anthropic, bukan di komputer — tetap jalan tanpa perubahan.
- **Memory & aturan** ada di repo ini (GitHub) — cukup clone.

## Yang dipasang di Mac mini Ubuntu

1. **Claude Code** — untuk kerja manual (seperti di Mac sekarang) dan untuk menjawab pesan Telegram.
2. **Repo metaads** di `~/metaads` (clone dari `khaeruddienfatih/metads`, push ke dua repo).
3. **Bot Telegram** `telegram/bot.py` — jalan terus sebagai service systemd (`elharamain-bot`).

## Langkah (sekali saja)

1. **Buat bot Telegram:** buka @BotFather di Telegram → `/newbot` → beri nama (mis. *Elharamain Iklan*) →
   simpan **token** yang diberikan. Jangan bagikan token ke siapa pun / jangan tulis di repo.
2. **Di Mac mini Ubuntu (Terminal):**
   ```bash
   curl -fsSLO https://raw.githubusercontent.com/khaeruddienfatih/metads/main/telegram/setup-ubuntu.sh
   bash setup-ubuntu.sh
   ```
   (kalau repo private: `git clone https://github.com/khaeruddienfatih/metads.git ~/metaads` dulu dengan login
   GitHub, lalu `bash ~/metaads/telegram/setup-ubuntu.sh`).
3. **Login Claude:** `claude` → ketik `/login` → pakai akun Claude yang sama (yang punya connector Meta Ads & Gmail).
   Cek connector: di dalam `claude` ketik `/mcp` → harus ada meta-ads & Gmail.
4. **Login GitHub** supaya Claude bisa commit/push catatan: `sudo apt install gh && gh auth login`.
5. **Isi token:** `nano ~/metaads/telegram/.env` → isi `TELEGRAM_BOT_TOKEN=...`.
   Jalankan `systemctl --user restart elharamain-bot`, lalu di Telegram kirim **/id** ke bot →
   salin angka chat ID ke `TELEGRAM_ALLOWED_CHAT_IDS=` di `.env` → restart lagi.
   (Bot hanya melayani chat ID yang terdaftar; orang lain diabaikan.)
6. **Tes:** kirim `/start`, lalu `/log`, lalu `/laporan`.

## Perintah di Telegram

| Perintah | Isi |
|---|---|
| `/laporan` | laporan chat & biaya hari ini s.d. sekarang (Umroh per akun, Haji per CS) |
| `/kemarin` | rekap kemarin |
| `/log` | 5 catatan kerja terakhir (chat-log) |
| `/routine` | jadwal routine otomatis |
| `/id` | chat ID Anda |
| teks bebas | diteruskan ke Claude Code di repo (mis. "cek iklan baru yang belum aktif") — 1–5 menit |

## Perawatan

- Log bot: `journalctl --user -u elharamain-bot -f`
- Restart: `systemctl --user restart elharamain-bot`
- Update kode bot setelah ada perubahan di repo: `cd ~/metaads && git pull && systemctl --user restart elharamain-bot`
- Bot memberi izin tool ke Claude lewat `--allowedTools` (Meta Ads, Gmail, Bash, Read, Edit, Write, Glob, Grep);
  ubah lewat `CLAUDE_ALLOWED_TOOLS` di `.env` kalau perlu.
- Aturan "iklan harus PAUSE kecuali diperintah" tetap berlaku: perintah lewat Telegram yang mengubah iklan
  (aktifkan, naik budget, hapus) dijalankan hanya kalau perintahnya eksplisit.
