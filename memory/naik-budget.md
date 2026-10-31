# Prosedur naik anggaran otomatis: CPR < Rp30rb 3 hari berturut-turut → +10%

Perintah user (31 Okt 2026): "jika setiap hari dalam 3 hari cpr bagus di bawah 30rb kamu naikan anggaran kampanyenya 10%".
Dijalankan tiap hari **04:00 WIB** sebagai langkah pertama routine "Jadwal pagi: ad set ON" (31 Okt, perintah user
"naik anggaran di jam 04 pagi"), SEBELUM ad set dinyalakan — supaya tidak bentrok (lihat `chat-memory.md`). Perintah ini mengalahkan aturan 24 Okt
"jangan ubah budget ad set yang sudah jalan" — khusus untuk kenaikan 10% ini.

## Akun (14)

Diana 1076195694707828 · Tira 868364731529534 · Nida 1019832712800468 · Hanif 482252744648260 ·
Allif 4678183395742010 · Fikri 1676215979752437 · AIni 814396810761205 · Irfan 1060984719243481 ·
Fifi 521083143750270 · Elharamain Haji 947788760498911 · Haji 2 1032468828178224 ·
Haji 3 794403715776985 · Haji 4 1526562231314028 · haji 1050343302646341

## Syarat (semua harus terpenuhi)

1. Campaign `effective_status` ACTIVE dan hasilnya chat WA (bukan pixel/add-to-cart).
2. Untuk **masing-masing** dari 3 hari terakhir (H-1, H-2, H-3, WIB; data per hari `time_increment "1"`):
   chat WA ≥ 1 **dan** spend ÷ chat **< Rp30.000**. Satu hari saja gagal (0 chat atau CPR ≥ Rp30rb) → tidak naik.
3. **Jeda 3 hari:** campaign ini tidak dinaikkan oleh prosedur ini dalam 3 hari terakhir (cek
   [`naik-budget-log.md`](naik-budget-log.md)). Jadi kenaikan berikutnya butuh 3 hari baru yang semuanya < Rp30rb.

## Batas maksimal (31 Okt, perintah user "batas maksimal budget 300rb perkampanye")

- Budget harian per campaign maksimal **Rp300.000**. CBO: baru = min(lama × 1,10 dibulatkan ke atas Rp1.000, Rp300.000).
  ABO: total budget ad set ACTIVE di campaign itu setelah naik ≤ Rp300.000 (kalau +10% melewati batas, naikkan tiap ad set
  dengan faktor yang sama sehingga total = Rp300.000, bulatkan ke bawah Rp1.000).
- Campaign yang budgetnya sudah ≥ Rp300.000 → tidak dinaikkan (dan TIDAK diturunkan), catat "sudah di batas".

## Cara naik

- **Budget di campaign (CBO, `daily_budget` campaign terisi):** `daily_budget` baru = lama × 1,10, dibulatkan ke atas
  ke Rp1.000. `ads_update_entity` (`ad_account_id`, `entity_id` = campaign, `fields {"daily_budget": <baru>}`).
  Pakai satuan yang sama dengan nilai `daily_budget` yang dibaca.
- **Budget di ad set (ABO):** naikkan `daily_budget` tiap ad set ACTIVE di campaign itu × 1,10 (dibulatkan ke atas Rp1.000).
- Budget lifetime → jangan diubah, laporkan saja.
- Jam 04:00 ad set masih PAUSED dari jadwal malam — itu normal; jangan nyalakan ad set di langkah ini (dinyalakan di langkah ON).
  Untuk ABO, budget ad set yang PAUSED tetap boleh dinaikkan kalau ad set itu ada di daftar jadwal malam (artinya ACTIVE sebelum 22:00).
- Setelah update: verifikasi `daily_budget` baru + `effective_status`. Kalau **campaign** jadi PAUSED karena update
  (ad set biarkan — dinyalakan langkah ON),
  aktifkan lagi (`ads_activate_entity` `object_ids`, `publish_as_active: true`; akun draft: kalau ditolak "no staged changes",
  ulangi dengan `entity_type` + `entity_id`). Kalau nilai belum berubah (akun mode draft → tersimpan sebagai draft),
  terbitkan dengan `ads_activate_entity` `object_ids` [id itu], `publish_as_active: true`.
- Ubah budget saja. Jangan sentuh targeting, penempatan, iklan.

## Pelaporan

- Tiap kenaikan: tambah baris di `memory/naik-budget-log.md`:
  `- YYYY-MM-DD | <akun> | <campaign_id> | <nama> | CBO/ABO | Rp<lama> → Rp<baru> | CPR H-3/H-2/H-1: Rp../Rp../Rp..`
- Entri chat-log + commit + push hanya kalau ada yang dinaikkan.
- Meta Ads: `client_conversation_id` `Hn4fT8qLz2WcP7xR1bVk`, `client_model` `claude-sonnet-5-5`.
