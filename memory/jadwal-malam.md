# Prosedur jadwal malam: ad set OFF jam 22:00, ON jam 04:00 WIB

Perintah user (31 Okt 2026): "saya mau setiap jam 11 malam adset off semua dan jam 4 pagi adset on" — dikoreksi user hari yang sama: **"matikan di jam 10 malam"** (OFF jam 22:00).
Dijalankan oleh 2 routine cloud (lihat `chat-memory.md`). Daftar ad set yang dimatikan disimpan di
[`jadwal-malam-daftar.md`](jadwal-malam-daftar.md), supaya jam 04:00 yang dinyalakan HANYA ad set itu.
Ad set yang sudah PAUSED sebelum jam 22:00 (dimatikan user, auto rule, atau cek tiap jam) tidak ikut dinyalakan.

## Akun (14)

Diana 1076195694707828 · Tira 868364731529534 · Nida 1019832712800468 · Hanif 482252744648260 ·
Allif 4678183395742010 · Fikri 1676215979752437 · AIni 814396810761205 · Irfan 1060984719243481 ·
Fifi 521083143750270 · Elharamain Haji 947788760498911 · Haji 2 1032468828178224 ·
Haji 3 794403715776985 · Haji 4 1526562231314028 · haji 1050343302646341

## OFF — jam 22:00 WIB

1. Per akun: `ads_get_ad_entities` level `adset`, filter `effective_status IN [ACTIVE]`, field `name, campaign_id, campaign_name, status, effective_status`.
   Ambil semua halaman (pagination). Akun yang error/IN_GRACE_PERIOD/tidak bisa dibaca → catat, lanjut akun lain.
2. Tulis daftar ke `memory/jadwal-malam-daftar.md` SEBELUM mem-pause (ganti seluruh isi file):
   judul `# Daftar ad set dimatikan jadwal malam — YYYY-MM-DD 22:00 WIB`, lalu satu baris per ad set:
   `- <ad_account_id> | <adset_id> | <nama ad set> | <campaign_name>`.
3. Pause tiap ad set: `ads_update_entity` `ad_account_id`, `entity_id` = ad set, `fields {"status":"PAUSED"}`.
   Ubah status saja. Jangan sentuh campaign, budget, targeting, iklan.
4. Verifikasi per akun (`ads_get_ad_entities` `object_ids`). Yang gagal di-pause: tandai baris di daftar dengan ` | GAGAL: <error>`.
5. Commit `memory/jadwal-malam-daftar.md` + entri chat-log, push.

## ON — jam 04:00 WIB

1. Baca `memory/jadwal-malam-daftar.md`. Pakai hanya kalau tanggal judulnya = kemarin (WIB). Kalau bukan → jangan nyalakan apa pun, laporkan.
2. Per ad set di daftar (lewati baris `GAGAL`): cek dengan `ads_get_ad_entities` `object_ids`.
   Nyalakan hanya kalau status sekarang PAUSED dan campaign-nya masih ACTIVE (kalau user mematikan campaign di malam hari, biarkan).
3. Nyalakan: `ads_activate_entity` `object_ids: [adset_id]`, `publish_as_active: true`. Kalau ditolak
   "has no staged changes in the draft" → ulangi dengan `entity_type: ad_set` + `entity_id` tanpa `object_ids`. Verifikasi.
4. Tulis di bawah daftar: `## Dinyalakan YYYY-MM-DD 04:00` + jumlah nyala / dilewati / gagal. Commit + chat-log, push.

## Catatan

- Cek tiap jam (`auto-reaktivasi.md`) dilewati pada jam 22:00–03:59 WIB supaya tidak menyalakan ad set di malam hari.
- Meta Ads: `client_conversation_id` `Hn4fT8qLz2WcP7xR1bVk`, `client_model` `claude-sonnet-5-5`.
