# Memory chat — pengisian iklan Umroh Elharamain Wisata (Meta Ads)

Ringkasan semua aturan, akun, dan hasil kerja dari sesi chat Claude (Sep–Okt 2026).
Teks iklan lengkap ada di [`primary-texts.md`](primary-texts.md).

## Aturan tetap dari user

- **Iklan harus PAUSE.** Jangan aktifkan/publish tanpa perintah eksplisit.
- **Model: selalu pakai Sonnet** (`claude-sonnet-5-5`), jangan Opus. Kirim `client_model` `claude-sonnet-5-5` di panggilan Meta Ads.
- **Maksimal 5 iklan per ad set.**
- **Gambar unik antar ad set** dalam satu campaign — jangan duplikasi iklan/gambar yang sama persis (user menghapus yang kembar). Default isi ad set kosong: 3 iklan, gambar berbeda-beda.
- **CTA WhatsApp** (`WHATSAPP_MESSAGE`), link `https://api.whatsapp.com/send`.
- **Page** `588336968031663` (Elharamain wisata), **IG user** `17841405431328414`.
- **Headline** berselang-seling:
  - `6700+ Google Review ⭐️⭐️⭐️⭐️⭐️ (5.0)`
  - `✈️ Tiket Sudah Confirm, Jadwal Pasti`
- **Deskripsi:** `Hotel Bintang 5 · Seat terbatas 45/keberangkatan`
- **Cloudinary aktif (sejak 9 Okt, perintah user): cloud `q2xuhm0o`** — URL `https://res.cloudinary.com/q2xuhm0o/image/upload/<public_id>.jpg`. Cloud lama `v6gwkqrb` tidak dipakai lagi.
  Materi Ramadhan: `Elharamainwisata/ramadhan`. Materi Haji: 9 gambar di root cloud ini. Materi Umroh lain (desember, januari, LAT, November) belum ada di cloud ini — minta user upload dulu.
- **Materi hanya dari folder Cloudinary** `Elharamainwisata/<folder>` (dulu `Elharamainwisata/Umroh/<folder>` di cloud lama); jangan ambil dari folder lain
  (mis. `Elharamainwisata/Fasilitas/fasilitas-maskapai-riyadh-air` **bukan** materi iklan).
- **Template WA** (diset manual oleh user di Ads Manager — tool tidak bisa):
  | Ad set | Template |
  |---|---|
  | November / Riyadh Air | `10 hari` (hanya untuk Riyadh Air) |
  | Desember | `9hari` |
  | 9 Hari Januari | `9hari` |
  | 12 Hari Januari | `12 Hari` |
  | LAT (Liburan Akhir Tahun) | LAT-1, 3, 5 → `9hari`; LAT-2, 4 → `12 Hari` |
| Ramadhan | belum ditentukan user |
- **Matikan "Media terkait"** (related media) di setiap iklan — manual di Ads Manager.
- **Naik anggaran:** update budget lewat tool memaksa kampanye aktif jadi PAUSED; user memilih
  "naikkan lalu aktifkan lagi".

## Folder Cloudinary (cloud lama `v6gwkqrb` — tidak dipakai lagi sejak 9 Okt; lihat catatan `q2xuhm0o` di bawah)

> **9 Okt:** connector Cloudinary sesi ini tersambung ke cloud **`q2xuhm0o`** (akun lain). Isinya hanya: `Elharamainwisata/ramadhan` (11 gambar Ramadhan, nama sama: Desain_2 #1–5, Desain_3 #1–6), `Elharamainwisata/Haji` (folder kosong), 9 gambar Haji di root (`1..6._Desain_Haji_Plus_Premium_...`, `1..3._Design_14_Haji_Plus_2027_...`), `main-sample`. Folder Umroh lain (desember, januari, LAT, November) **tidak ada** di cloud ini. Cek cloud name dari `secure_url` sebelum pakai URL.

| Folder | Isi |
|---|---|
| `Umroh/November` | `10_Hari_Riyad_Air_1..5` + desain baru `1..6._Desain_2_Paket_Umroh_Musim_Sejuk_Premium_Umroh_10_Hari_By_Riyadh_Air_...` (30 Sep) |
| `Umroh/desember` | gambar `saudia_9_hari_1..10`, video `saudia_9_hari_1..5, 10..13` |
| `Umroh/januari 9 hari` | gambar+video `januari_1..8`, desain `Desain_3/Desain_4_Paket_Umroh_Januari...` |
| `Umroh/12 hari januari` | gambar `12_hari_januari_1..5`, video `12_hari_januari_1..4` |
| `Umroh/Liburan Akhir Tahun` | `Desain_Paket 1..4`, `Desain_2_Paket 1..4`, `Desain_3_Paket 1..4` |
| `Umroh/Ramadhan` | (8 Okt) 11 gambar: `1..5._Desain_2_Paket_Umroh_Ramadhan_Musim_Dingin_By_Saudia_Airlines_...` + `1..6._Desain_3_Paket_Umroh_Ramadhan_...`. Teks iklan: bagian **Ramadhan** di `primary-texts.md` |

## Catatan teknis Meta Ads MCP

- **Izin otomatis (9 Okt):** user menambahkan `.claude/settings.json` (allow-list: baca Meta Ads, buat creative/iklan, `ads_update_entity`, baca Cloudinary, git). Aktivasi & hapus iklan sengaja tidak di-allow. Berlaku mulai sesi baru.

- **Akun Elharamain Haji (947788760498911):** Page iklan beda per kampanye — **tiru Page/IG dari iklan lama kampanye itu** (cek `ads_get_creatives` → `effective_object_story_id`). Kampanye **Irfan** pakai Page `588336968031663` + IG `17841405431328414` (bukan Page Haji `637020022834756`); Diana pakai Page Haji tanpa IG. Cara yang disukai user untuk kampanye Irfan: duplikat iklan yang ada lalu ganti gambar. Materi Haji di Cloudinary `Elharamainwisata/Haji` (gambar Desain/Premium + video Hajj_2025-46..63). **User minta iklan baru, jangan salin/pakai ulang iklan atau creative yang sudah ada** (5 Okt). Creative lama di akun ini terikat Page; creative Irfan tidak cocok untuk ad set lain.

- `client_conversation_id` yang dipakai: `Hn4fT8qLz2WcP7xR1bVk` (`client_model`: `claude-sonnet-5-5`).
- **Akun mode draft** (Diana, Hanif, AIni, Fikri; Fifi & Irfan & Tira ternyata live, langsung PAUSED): iklan dibuat sebagai DRAFT, status spec ACTIVE → setelah
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
| Tira | 868364731529534 | 85 iklan PAUSED di 17 ad set. **8 Okt: campaign Ramadhan (`120252500197150584`) 3 ad set "Ramadhan" (…197250584/…197270584/…197260584) diisi 9 iklan PAUSED (Ramadhan Desain_2 #1–5 + Desain_3 #1–4, teks Ramadhan, headline berselang-seling).** 4 Okt: campaign **Desember** (`120252435431070584`) 3 ad set "Desember" kosong: 15 iklan salinan sempat dibuat lalu **dihapus user (gambar kembar)**; diisi ulang 3 iklan/ad set dengan gambar beda (saudia_9_hari_1–9, PAUSED). Iklan Riyadh Air Tira terbaca ACTIVE (kemungkinan diaktifkan user). 3 Okt: campaign **November** (`120252381981140584`) +9 iklan Riyadh Air PAUSED (akun live, bukan draft), 3/ad set |
| Nida | 1019832712800468 | 30 iklan PAUSED di 6 ad set. **9 Okt: campaign Ramadhan (`120251621058780004`) 3 ad set "Ramadhan" (…058850004/…058880004/…058840004) diisi 9 draft PAUSED (Ramadhan Desain_2 #1–5 + Desain_3 #1–4, gambar dari cloud q2xuhm0o via creative dummy `upload Ramadhan …`).** Ad set desember lama (`120251397671600004`, campaign "Nida") hanya 4 iklan — **user minta stop dulu, jangan diubah** |
| Hanif | 482252744648260 | **9 Okt: campaign Ramadhan (`120254754061360427`) 3 ad set "Ramadhan" (…061420427/…061480427/…061410427) diisi 9 draft PAUSED (Ramadhan Desain_2 #1–5 + Desain_3 #1–4, cloud q2xuhm0o).** 25 draft dibuat ulang (fix CTA), PAUSED; 24 draft lama `XXX HAPUS - ERROR` perlu discard manual. 3 Okt: campaign **Riyadh Air** (`120254662875790427`) +9 draft PAUSED (3/ad set: Desain 2 #1–3, Desain 2 #4–6, 10_Hari_Riyad_Air 1–3) |
| Elharamain Wisata / Allif (bisnis Elharamain Haji) | 4678183395742010 | Campaign **Alif**: 25 iklan PAUSED (gambar+video dari Cloudinary). 5 Okt: campaign Desember (`120252148895910228`) 3 ad set kosong diisi 9 iklan PAUSED (saudia 1–9); akun live. 6 Okt: 6 ad set kosong diisi 3 iklan PAUSED (18 iklan): campaign 9 Januari (`120252169243440228`, ad set …43460228/…43450228/…43430228, januari_1–8 + Desain_3 #1) dan Liburan Akhir Tahun (`120252169205320228`, ad set …05430228/…05420228/…05410228, desain LAT 9 gambar). Ad set Desember `120252083784810228` (campaign 120252083784770228) baru 2 iklan (video saja) — belum disentuh. 7 Okt: campaign baru (`120252189006530228`) 3 ad set kosong diisi 9 iklan PAUSED: Riyad AIr `120252189006570228` (Desain 2 #1–3, teks Riyadh), Desember `120252189006690228` (saudia 4–6), AKhir Tahun `120252189006700228` (LAT 1–3). Iklan lama banyak ACTIVE; ad set 9 Januari `120252169243460228` terbaca PAUSED (kemungkinan dipause user) |
| Elharamain Fifi | 1676215979752437 | Campaign **Fikri** (draft): 25 iklan gambar-only PAUSED; Riyadh Air pakai desain baru 1–5. **9 Okt: campaign Ramadhan (`120249566336610470`) 3 ad set (Ramadhan - 1 …690470, Ramadhan - 2 …700470, Ramadhan …710470) diisi 9 draft PAUSED (Ramadhan Desain_2 #1–5 + Desain_3 #1–4, cloud q2xuhm0o)** |
| Elharamain Haji | 947788760498911 | 29 Sep: budget 6 kampanye aktif +15% lalu diaktifkan lagi. Akun LIVE, konten Haji. 5 Okt: ad set <3 iklan diisi dengan salinan creative (PAUSED) → 9 iklan baru; 5 Okt: kampanye Diana (`120250519255890739`, budget Rp270.000) 4 ad set baru (LLA/Interest/broud/Retargeting, semua PAUSED) diisi 12 iklan BARU PAUSED (materi folder Haji, bukan salinan); 5 Okt (lanjutan): semua ad set di semua kampanye (AIni, Nida, Hanif, Fikri, Tira, Irfan) diisi iklan BARU PAUSED sampai ≥3 iklan (17 iklan); ad set kosong baru Tira Broud `120250695823180739` & Irfan Retargeting `120250695786990739` ikut terisi. Iklan salinan lama sudah dihapus user. Page `637020022834756` bisa dipakai di ad set Irfan juga |
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
- 8 Okt: user **menolak** pause lanjutan iklan Riyadh Air/November/LAT di Irfan (5 iklan LAT ad set `120253100040430414`) — jangan lanjutkan pause tanpa perintah baru.
- Template WA untuk iklan Ramadhan belum ditentukan.

## Riyadh Air — sebaran per akun (3 Okt 2026)

Hasil scan semua akun (ad set bernama "Riyadh Air"). Ad set kosong diisi 3 iklan PAUSED
(Desain 2 #1–3, #4–6, 10 Hari 1–3). Ad set yang sudah 5 iklan tidak disentuh.

| Akun | ID | Status |
|---|---|---|
| Hanif | 482252744648260 | 3 ad set diisi (9 draft). 5 Okt: campaign Desember (`120254685722760427`) 3 ad set kosong diisi 9 draft PAUSED (saudia 1–9) |
| Tira | 868364731529534 | 3 ad set diisi (9 iklan) |
| AIni | 814396810761205 | 3 ad set diisi (9 draft). 5 Okt: campaign Riyadh Air direstruktur (`120253589562730019`); +21 draft PAUSED di 7 ad set kosong lain (Desember ×5, 9 Hari Januari, LAT), 3/ad set gambar unik; 6 Okt: 6 ad set kosong lagi diisi 18 draft PAUSED (3/ad set): campaign 9 Januari (`120253612138060019`, ad set …138100019/…138080019/…138070019, 9 gambar januari) dan Liburan AKhir Tahun (`120253612013570019`, ad set …013690019/…013680019/…013620019, 9 gambar LAT). Semua ad set AIni sekarang ≥3 iklan |
| Irfan | 1060984719243481 | 3 ad set baru diisi (9 iklan); 3 ad set lain sudah 5 iklan. 5 Okt: campaign Desember (`120253231255400414`) 3 ad set kosong diisi 9 iklan PAUSED (saudia 1–9) |
| Diana | 1076195694707828 | 3 ad set diisi (9 draft). 5 Okt: campaign Desember (`120251937346180294`) 3 ad set kosong diisi 9 draft PAUSED (saudia 1–9) |
| Fikri | 1676215979752437 | 3 ad set baru diisi (9 draft); 3 ad set lain sudah 5 iklan. 5 Okt: campaign Desember (`120249501856030470`) 3 ad set kosong diisi 9 draft PAUSED (saudia 1–9) |
| Fifi | 521083143750270 | 1 ad set diisi (3 iklan); 2 lain sudah 5 iklan. 4 Okt: campaign "Riyad Air" (`120252308382230365`), 3 ad set diisi (9 iklan, live PAUSED). 5 Okt: campaign Saudia (`120252109559290365`) 2 ad set "Desember" kosong diisi 6 iklan PAUSED (saudia 1–6); 6 Okt: 2 campaign baru, 6 ad set kosong diisi 3 iklan PAUSED (18 iklan, akun live): LAT (`120252329548970365`: ad set 120252329549000365/…48990365/…48980365, gambar Liburan Akhir Tahun, teks LAT) dan Desember (`120252329530240365`: ad set 120252329530320365/…30310365/…30300365, saudia 1–9, teks Desember). Di akun live, `link_data.picture` (URL Cloudinary) bisa dipakai tanpa upload hash. Ad set Fifi dengan 1–2 iklan (Januari 1; Saudia 12 Hari, Saudia, Saudia 120252109559410365 masing-masing 2) belum disentuh |
| Nida | 1019832712800468 | campaign Riyadh Air (`120251511582700004`), 3 ad set "Riyad Air" diisi (9 draft). 5 Okt: campaign Desember (`120251555363950004`) 3 ad set kosong diisi 9 draft PAUSED (saudia 1–9) |
| Allif | 4678183395742010 | campaign Riyadh Air (`120252087342810228`), 3 ad set "Riyad Air" diisi (9 iklan, live). Ad set "Riyad AIr" di campaign Alif/Alif INDO tidak disentuh |
| CloseF | 1050343302646341 | 1 ad set, sudah 5 iklan (tidak disentuh) |

**Ejaan ad set bervariasi** ("Riyadh Air", "Riyad Air", "Riyad AIr") — scan pakai kata kunci `Riyad`. Rescan 3 Okt: tidak ada tambahan selain tabel ini. Akun tanpa ad set Riyadh Air: Elharamain Haji, dll. Akun Ads MCP belum dibuka
(Elharamainclose, Umroh Plus, Elharamainwisata, dll.) tidak bisa dicek.

## Pending (8 Okt 2026)

- Tugas "matikan iklan Riyadh Air + November + Liburan Akhir Tahun di semua akun Umroh" baru selesai untuk AIni, Tira, dan sebagian Irfan. Sisa akun ada di `chat-log.md` (entri 7 Okt).
