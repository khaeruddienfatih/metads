# Memory chat — pengisian iklan Umroh Elharamain Wisata (Meta Ads)

Ringkasan semua aturan, akun, dan hasil kerja dari sesi chat Claude (Sep–Okt 2026).
Teks iklan lengkap ada di [`primary-texts.md`](primary-texts.md).

## Aturan tetap dari user

- **Iklan harus PAUSE.** Jangan aktifkan/publish tanpa perintah eksplisit.
- **Model: selalu pakai Sonnet** (`claude-sonnet-5-5`), jangan Opus. Kirim `client_model` `claude-sonnet-5-5` di panggilan Meta Ads.
- **Maksimal 5 iklan per ad set.**
- **CTA WhatsApp** (`WHATSAPP_MESSAGE`), link `https://api.whatsapp.com/send`.
- **Page** `588336968031663` (Elharamain wisata), **IG user** `17841405431328414`.
- **Headline** berselang-seling:
  - `6700+ Google Review ⭐️⭐️⭐️⭐️⭐️ (5.0)`
  - `✈️ Tiket Sudah Confirm, Jadwal Pasti`
- **Deskripsi:** `Hotel Bintang 5 · Seat terbatas 45/keberangkatan`
- **Materi hanya dari folder Cloudinary** `Elharamainwisata/Umroh/<folder>`; jangan ambil dari folder lain
  (mis. `Elharamainwisata/Fasilitas/fasilitas-maskapai-riyadh-air` **bukan** materi iklan).
- **Template WA** (diset manual oleh user di Ads Manager — tool tidak bisa):
  | Ad set | Template |
  |---|---|
  | November / Riyadh Air | `10 hari` (hanya untuk Riyadh Air) |
  | Desember | `9hari` |
  | 9 Hari Januari | `9hari` |
  | 12 Hari Januari | `12 Hari` |
  | LAT (Liburan Akhir Tahun) | LAT-1, 3, 5 → `9hari`; LAT-2, 4 → `12 Hari` |
- **Matikan "Media terkait"** (related media) di setiap iklan — manual di Ads Manager.
- **Naik anggaran:** update budget lewat tool memaksa kampanye aktif jadi PAUSED; user memilih
  "naikkan lalu aktifkan lagi".

## Folder Cloudinary (cloud `v6gwkqrb`)

| Folder | Isi |
|---|---|
| `Umroh/November` | `10_Hari_Riyad_Air_1..5` + desain baru `1..6._Desain_2_Paket_Umroh_Musim_Sejuk_Premium_Umroh_10_Hari_By_Riyadh_Air_...` (30 Sep) |
| `Umroh/desember` | gambar `saudia_9_hari_1..10`, video `saudia_9_hari_1..5, 10..13` |
| `Umroh/januari 9 hari` | gambar+video `januari_1..8`, desain `Desain_3/Desain_4_Paket_Umroh_Januari...` |
| `Umroh/12 hari januari` | gambar `12_hari_januari_1..5`, video `12_hari_januari_1..4` |
| `Umroh/Liburan Akhir Tahun` | `Desain_Paket 1..4`, `Desain_2_Paket 1..4`, `Desain_3_Paket 1..4` |

## Catatan teknis Meta Ads MCP

- `client_conversation_id` yang dipakai: `Hn4fT8qLz2WcP7xR1bVk` (`client_model`: `claude-sonnet-5-5`).
- **Akun mode draft** (Diana, Hanif, Fifi): iklan dibuat sebagai DRAFT, status spec ACTIVE → setelah
  dibuat, set `status: PAUSED` via `ads_update_entity`. Draft tidak bisa dihapus lewat tool; yang
  rusak di-rename `XXX HAPUS - ERROR` + PAUSED, user discard manual.
- Di draft, creative **harus pakai `image_hash`** (bukan `image_url`) → kalau tidak, error
  `ObjectStorySpecRedundant`.
- **Error CTA "Link Title and Link Description Are Deprecated"**: muncul kalau creative dibuat lewat
  `ads_create_creative` dengan headline/description (tool memasukkan `link_title`/`link_description`
  ke CTA). Solusi: buat iklan dengan **inline `object_story_spec`**:
  `link_data{link, message, name, description, image_hash, call_to_action{type, value{link}}}`
  (video: `video_data{video_id, image_hash, message, title, link_description, call_to_action}`).
- `ads_creative_upload_media` belum dibuka untuk akun Nida, Hanif, Fifi. Workaround: buat
  creative dummy `ads_create_creative` dengan `image_url` Cloudinary → gambar masuk library, lalu
  ambil `image_hash` via `ads_get_creatives` (creative dummy dinamai `upload …`, tidak dipakai).
- Image hash = hash konten, sama di semua akun untuk file yang sama.

## Status per akun

| Akun | ID | Hasil |
|---|---|---|
| Diana | 1076195694707828 | 35 iklan non-IG ACTIVE; 5 ad set campaign IG ARCHIVED (belum dikonfirmasi user) |
| Tira | 868364731529534 | 85 iklan PAUSED di 17 ad set |
| Nida | 1019832712800468 | 30 iklan PAUSED di 6 ad set. Ad set desember lama (`120251397671600004`, campaign "Nida") hanya 4 iklan — **user minta stop dulu, jangan diubah** |
| Hanif | 482252744648260 | 25 draft dibuat ulang (fix CTA), PAUSED; 24 draft lama `XXX HAPUS - ERROR` perlu discard manual. 3 Okt: campaign **Riyadh Air** (`120254662875790427`) +9 draft PAUSED (3/ad set: Desain 2 #1–3, Desain 2 #4–6, 10_Hari_Riyad_Air 1–3) |
| Elharamain Wisata (bisnis Elharamain Haji) | 4678183395742010 | Campaign **Alif**: 25 iklan PAUSED (gambar+video dari Cloudinary) |
| Elharamain Fifi | 1676215979752437 | Campaign **Fikri** (draft): 25 iklan gambar-only PAUSED; Riyadh Air pakai desain baru 1–5 |
| Elharamain Haji | 947788760498911 | 29 Sep: budget 6 kampanye aktif +15% lalu diaktifkan lagi |
| Elharamainclose | 1401255787216018 | Ads MCP belum dibuka |

### Budget Elharamain Haji (947788760498911), per 2 Okt 2026

| Kampanye | Budget harian |
|---|---|
| Diana (baru) | Rp250.000 |
| Irfan | Rp230.000 |
| AIni | Rp287.500 |
| Nida | Rp287.500 |
| Fikri | Rp287.500 |
| Tira | Rp402.500 |
| Hanif | Rp287.500 |

Kenaikan 15% kedua (2 Okt) **dilakukan manual oleh user** di Ads Manager — angka di atas adalah
nilai sebelum kenaikan itu.

## Pending / pertanyaan terbuka

- Diana: 5 ad set IG ARCHIVED — disengaja?
- Nida desember lama: 4 iklan — ditunda atas permintaan user.
