# Memory chat — pengisian iklan Umroh Elharamain Wisata (Meta Ads)

Ringkasan semua aturan, akun, dan hasil kerja dari sesi chat Claude (Sep–Okt 2026).
Teks iklan lengkap ada di [`primary-texts.md`](primary-texts.md).

## Aturan tetap dari user

- **Panggil user "Juragan" (3 Nov, perintah user "kamu panggil saya juragan").** Sapa dengan "Juragan" saat menjawab.
- **Tujuan performa default (22 Okt):** semua objective (penjualan/prospek/interaksi/traffic) pakai **percakapan pesan dimulai** (`CONVERSATIONS`, destinasi WHATSAPP).
- **Pesan pembuka WA / ice breakers (22 Okt):** "Assalamualaikum info paket umrah Elharamain Wisata Terimakasih", "Assalamualaikum info paket umrah 9 Hari Elharamain Wisata Terimakasih", "Assalamualaikum info paket umrah 12 Hari Elharamain Wisata Terimakasih"; **iklan Ramadhan (22 Okt): tambah "Assalamualaikum info paket umrah Ramadhan Elharamain Wisata Terimakasih" di urutan pertama**; sambutan: "Assalamualaikum Warahmatullahi Wabarakatuh, Elharamain Wisata Siap Melayani Anda" (link_data.page_welcome_message). Nomor WA per akun hanya bisa dipasang lewat tool kalau akun FB connector punya akses ke aset nomor WA di Business Settings (22 Okt: belum punya → error 4017029).
- **Penempatan berbasis data chat (29 Okt, perintah user untuk campaign Sales Tira):** IG Feed + IG Story + IG Reels + FB Feed + FB Story + FB Reels + WA Status + **Threads (user minta tetap dimasukkan karena masih baru; Meta belum menayangkannya untuk iklan WA)** — tanpa IG Explore/Profile/Search. 29 Okt: user minta "coba beberapa akun dulu" — diterapkan HANYA ke ad set baru (ad set lama/berjalan tidak diubah); akun uji selain Tira belum dipilih user.
- **Penempatan default (22 Okt):** setiap iklan baru → penempatan ad set: **semua Instagram + Facebook Story + WhatsApp Status + Threads** (spec di [`target-kota.md`](target-kota.md)). Jangan pakai IG `explore` (deprecated).
- **Target kota default (22 Okt):** setiap iklan baru → lokasi ad set-nya diganti sesuai daftar di [`target-kota.md`](target-kota.md) (25 kota radius 40 km + 5 subcity Jakarta, dari campaign Sales AIni). Ganti hanya `geo_locations`, bagian targeting lain tetap. Ad set yang namanya menunjuk wilayah tertentu (jakarta/jabar/jatim/banten/Depok/Bandung, dll.) — tanyakan dulu sebelum diganti. Perubahan targeting di akun draft tersimpan sebagai draft → publish hanya dengan perintah user.
- **Paket Riyadh Air / November sudah tidak ada (20 Okt).** Teksnya dihapus dari `primary-texts.md`; jangan buat iklan Riyadh Air lagi.
- **Semua paket pakai pesawat Saudia Airlines (20 Okt).** Setiap adcopy wajib ada `By Saudia Airlines` di judul + `✅Pesawat Direct Flight by Saudia`.
- **Git: hanya pakai branch `main`.** Jangan buat branch baru (11 Okt) — commit & push langsung ke `main`.
- **Semua campaign baru wajib sesuai target kota & penempatan default (22 Okt)** — termasuk ad set ACTIVE yang belum punya iklan berjalan; cek ulang setelah user menyalin/menerbitkan (Meta bisa mengubah Prospek jadi Hong Kong/Indonesia + penempatan otomatis).
- **Jangan sentuh iklan/ad set yang sedang berjalan (ACTIVE) (22 Okt).** Perbaikan (lokasi, penempatan, dll.) hanya untuk yang PAUSED/draft; yang ACTIVE dilaporkan saja.
  **24 Okt (perintah user): "jangan di ganggu adset yang sudah jalan beberapa hari"** — ad set yang sudah tayang >1 hari JANGAN diubah sama sekali (lokasi, penempatan, budget, iklan). Pengecualian hanya ad set yang baru aktif hari itu (created/start hari ini, spend ≈ 0) kalau user minta; setelah update yang memaksa PAUSED, aktifkan lagi ke status semula.
- **Buat iklan BARU, jangan duplikat (24 Okt, perintah user).** Isi/perbaiki ad set selalu dengan iklan baru (inline `object_story_spec`: link_data message/name/description/image_hash + CTA tanpa link_title/link_description), JANGAN salin via `source_ad_id`/`creative_id` — salinan di akun draft gagal terbit (error 1815589 "Link Title and Link Description Are Deprecated").
- **Nama campaign diawali tujuan (24 Okt, perintah user):** campaign Penjualan (OUTCOME_SALES) → awalan `Sales …`, Prospek (OUTCOME_LEADS) → `Prospek …`, lalu wilayah (mis. `Sales jawa barat`, `Prospek banten`).
- **Campaign bernama wilayah → lokasi ad set sesuai wilayah (24 Okt, perintah user):** campaign `… jawa barat` → kota Jawa Barat, `… banten` → kota Banten, `… jakarta` → Jakarta + 5 subcity (daftar kelompok di [`target-kota.md`](target-kota.md), radius 40 km). Nama ad set diberi akhiran wilayah (mis. `9 januari - Jawa Barat`). Ini menggantikan default 25 kota untuk campaign wilayah.
- **Akun Haji (1050343302646341) — umur 30–50 (24 Okt, perintah user).** Akun iklan Haji yang dipakai user = `1050343302646341` (dulu tercatat "CloseF"). Ad set non-wilayah di akun ini → 25 kota default. Agar umur 30–50 diterima: set `targeting_automation.individual_setting.age=0` (kalau 1 → error 1870188). Akun ini mode DRAFT.  Iklan di akun ini pakai Page `588336968031663` + IG `17841405431328414` (Page Haji 637020022834756 ditolak: error 1885029 "Pages Don't Match"). Tiap campaign 5 ad set: Jakarta, Jawa Barat, Banten, Jawa (+ Surabaya 992951), Luar Pulau. **25 Okt: 9 campaign "- Salin" + 45 ad set + 135 iklan DIAKTIFKAN atas perintah user (Rp120rb/hari per campaign).**
- **Umur Haji 35–55 (5 Nov 2026, user: "khusus haji umur beda dari 35-55").** Semua ad set Haji (akun Elharamain Haji, Haji 2/3/4, haji) memakai umur 35–55. Di akun dengan Advantage+ Audience, Meta menolak umur minimal > 25 sebagai batas keras → pasang `age_min` 25, `age_max` 65 + `age_range` [35,55] (saran), `targeting_automation.advantage_audience` 1. (Aturan lama "Akun Haji 1050343302646341 umur 30–50" diganti 35–55.) Umroh tetap 25–65+.
- **Umur default 25–65+ (24 Okt, perintah user)** untuk ad set baru, bersama penempatan default (semua IG + FB Story + WA Status + Threads, mobile+desktop).
- **Cek tiap jam auto rule (30 Okt, perintah user):** ad set yang dimatikan auto rule user hari ini & CPR hari ini < Rp35rb (≥1 chat; naik dari 30rb, 1 Nov) dinyalakan lagi otomatis **tanpa batas berapa kali per hari dan tanpa syarat CPR 3 hari (dihapus 3 Nov, perintah user "perhari")** — prosedur di [`auto-reaktivasi.md`](auto-reaktivasi.md). Sejak 30 Okt berjalan sebagai **routine cloud** `trig_01PExMLpwLUtZxVRsi4R6e8H` (tiap jam menit :13, Sonnet, connector Meta-Ads) — tetap jalan walau komputer mati; kelola/hapus di https://claude.ai/code/routines. Cron lokal sudah dihapus.
- **Jadwal malam (31 Okt, perintah user "setiap jam 11 malam adset off semua dan jam 4 pagi adset on"):** routine cloud `trig_01FPcdHh57QKkum5LoEAwj2k` tiap **22:00 WIB** (dikoreksi user dari 23:00: "matikan di jam 10 malam") mem-PAUSE semua ad set ACTIVE di 14 akun & menyimpan daftarnya di [`jadwal-malam-daftar.md`](jadwal-malam-daftar.md); routine `trig_01KLe5sJc8N6MQMEYKUpzNqB` tiap 04:00 WIB menyalakan lagi HANYA ad set di daftar itu (yang masih PAUSED & campaign ACTIVE). Cek tiap jam dilewati 22:00–03:59. Prosedur: [`jadwal-malam.md`](jadwal-malam.md).
- **Naik anggaran otomatis (31 Okt, perintah user "jika setiap hari dalam 3 hari cpr bagus di bawah 30rb kamu naikan anggaran kampanyenya 10%"):** **sejak 31 Okt jalan jam 04:00 WIB sebagai langkah pertama routine Jadwal pagi ON `trig_01KLe5sJc8N6MQMEYKUpzNqB`** (routine terpisah `trig_01XvAgB4noayYxfMXZgoiruc` 07:00 dinonaktifkan); **batas maks Rp300rb/hari per campaign** (tidak diturunkan kalau sudah di atas); **akun Allif 4678183395742010 DIKECUALIKAN — tidak boleh dinaikkan walau ada pemenang (1 Nov, perintah user)** — campaign ACTIVE (chat WA) yang H-1, H-2, H-3 masing-masing ≥1 chat & CPR < Rp30rb → daily budget +10% (CBO di campaign, ABO di tiap ad set ACTIVE), dibulatkan ke atas Rp1.000, lalu aktif lagi. Jeda 3 hari antar kenaikan per campaign. Log: [`naik-budget-log.md`](naik-budget-log.md), prosedur: [`naik-budget.md`](naik-budget.md). Mengalahkan aturan 24 Okt soal budget ad set berjalan, khusus kenaikan ini.
- **Cek tiap 30 menit (1 Nov, perintah user):** routine cloud `trig_01PExMLpwLUtZxVRsi4R6e8H` (menit :13) + `trig_013WfwoGnfBo14J4EupZGgtx` (menit :43) menjalankan [`auto-reaktivasi.md`](auto-reaktivasi.md): A nyalakan ad set rule-off CPR hari ini < Rp35rb (1 Nov 16:15: naik dari 30rb) (user: "ganti jadi per 30 menit juga"); B pause ad set hari ini (≥ Rp30rb & 0 chat) ATAU (> Rp40rb & < 2 chat); C pause iklan CPR sepanjang waktu > Rp50rb (atau 0 chat & ≥ Rp35rb). Jendela malam 22:00–03:59 dilewati.
- **Ad set boros per hari (30 Okt, perintah user "matikan adset yang habis 25ribu tapi tidak ada chat"):** ad set ACTIVE dengan spend hari ini ≥ Rp30rb (naik dari 25rb, 30 Okt) dan 0 chat WA → PAUSE otomatis tiap jam (Bagian B di [`auto-reaktivasi.md`](auto-reaktivasi.md), routine cloud yang sama). Ad set non-chat (pixel/add-to-cart) dikecualikan.
- **Tabel pengeluaran bulan berjalan (4 Nov, user: "laporan setiap pagi itu ada laporan pengeluaran mulai tanggal 1 sampai tanggal saat ini dalam bentuk table di bawah"):** email pagi 06:00 & 08:00 punya tabel paling bawah "Pengeluaran <tgl 1> s.d. <kemarin> per akun" (biaya, chat, CPR per akun Umroh/Haji) — `tabel_bawah` di `tools/laporan_email_html.py`, dicek `tools/cek_laporan.py`.
- **Email laporan pagi (30 Okt, perintah user; jam diubah 31 Okt):** tiap hari **06:00 WIB** routine cloud `trig_01Ci9E1ffEGZ97CAaxiyqCBY` mengirim ke **elharamainwisata@gmail.com** (1 Nov: diganti dari khaeruddien@gmail.com, perintah user), dan tiap **08:00 WIB** routine `trig_01NydaDZaZmHdb68jLxpn13R` mengirim laporan yang sama ke **dhiyaaelhaq01@gmail.com** (31 Okt, perintah user) — jumlah chat WA + biaya + CPR kemarin dalam bentuk TABEL (30 Okt: user minta "kirim dalam bentuk table"), Umroh vs Haji per akun (campaign "Yoga" di akun Haji 947… dihitung Umroh; biaya pixel non-chat dicatat terpisah). Read-only. **1 Nov (perintah user "kirim setiap pagi siang sore dan malam jam 21"):** routine `trig_01D9NHsCepUj6rvi7cs5nt77` tiap **12:00, 16:00, 21:00 WIB** mengirim laporan HARI INI s.d. jam itu (chat, biaya, CPR per akun Umroh/Haji, TANPA pembanding kemarin — user: "cukup perhari saja tidak perlu di bandingkan") ke elharamainwisata@gmail.com. **1 Nov ("nanti laporan begini juga ya bagian hajinya"):** semua email laporan (06:00, 08:00, 12/16/21) bagian Haji = tabel **Haji per CS** (campaign Haji digabung per nama CS lintas akun Haji) + tabel Haji per akun + catatan CS CPR terendah / > Rp40rb / 0 chat. **1 Nov ("pakai table dan sortir dari anggaran terbesar"):** semua email = tabel HTML dibangun dengan `tools/laporan_email_html.py` (style inline + salam pembuka & penutup; jangan tulis HTML manual; tanggal WAJIB dari `tools/tanggal_laporan.py`; WAJIB lolos `tools/cek_laporan.py` sebelum kirim, gagal → laporan pimpinan tidak dikirim; tanpa perbandingan hari sebelumnya — user 2 Nov "ga perlu ada perbandingan kemarin"), subjek `Laporan Iklan Elharamain Wisata <DD Mon YYYY> (Rekap Harian | Siang | Sore | Malam)`, baris per akun/per CS diurutkan dari **biaya terbesar**, kolom Biaya | Chat | CPR.
- **Laporan WAJIB dicek seperti pimpinan (5 Nov, user: "untuk tira jadi keributan di team kamu harus bener bener cek" + "sekecil apapun itu jadi keributan di team kami" + "kamu jadi pimpinan harus cek bener bener jangan asal asalan pekerjaan saya pertaruhannya").** Penyebab: laporan pimpinan 04 Nov melewatkan campaign Tira "new" (Rp141rb, 1 chat; 1–4 Nov ±Rp735rb). Sekarang: (1) setiap laporan punya "kontrol" per akun = biaya level akun dari Meta + SEMUA campaign; `tools/cek_laporan.py` GAGAL kalau jumlah campaign ≠ biaya akun, baris tabel ≠ kontrol, atau Anggaran ≠ total biaya akun 1 s.d. kemarin; (2) laporan pimpinan 08:00 = SALINAN PERSIS email 06:00 (dibaca dari Gmail terkirim), tidak query Meta ulang — angka pimpinan & elharamainwisata selalu sama; hanya kalau 06:00 gagal, 08:00 hitung sendiri dengan kontrol. Saat Claude sendiri membuat laporan/angka: selalu cocokkan total per akun dengan biaya level akun sebelum kirim.
- **Ad set selalu ikut SOP kecuali user minta lain (4 Nov, user: "kan sudah saya bilang adset sesuai arahan saya" → "maksudnya yang kamu pakai sop kecuali saya minta").** Saat mengisi iklan, langsung samakan ad set dengan SOP (26 kota default/wilayah, penempatan default, umur 25–65+) tanpa bertanya — kecuali user memberi arahan khusus untuk ad set itu. Batasan SOP lain tetap: ad set yang sudah tayang >1 hari tidak diubah; ad set bernama wilayah tertentu ikut kelompok wilayahnya.
- **Iklan harus PAUSE.** Jangan aktifkan/publish tanpa perintah eksplisit.
- **Model: pakai Opus** (`claude-opus-5-5`) sejak 4 Nov (perintah user "model ganti pakai opus sonet kamu suka ngaco") — menggantikan aturan lama "selalu Sonnet". Kirim `client_model` `claude-opus-5-5` di panggilan Meta Ads saat sesi berjalan di Opus. **Routine cloud tetap Sonnet** (4 Nov, perintah user "routine biarkan pakai sonet") — jangan diubah ke Opus.
- **Maksimal 5 iklan per ad set.**
- **Iklan boros (20 Okt):** iklan yang total spend ≥ Rp35.000 dengan hasil 0 sepanjang tayang → dihapus (DELETED, user pilih hapus permanen). Sudah dijalankan di Fifi (3 iklan), 9 akun kerja, dan akun haji (20 Okt). Akun mode draft: stage DELETED lalu publish hanya iklan itu.
- **Pakai ulang iklan bagus (21 Okt):** bisa pakai post iklan lain via `object_story_id` (`ads_get_creatives` → `effective_object_story_id`) + `instagram_user_id`, juga lintas akun asal Page sama (588336968031663). Hanya kalau teks post sudah sesuai aturan (By Saudia + Direct Flight); kalau belum, buat iklan baru dengan gambar pemenang + teks terbaru. **30 Okt (perintah user "boleh pakai asal sesuai page dan paket"): post pemenang boleh dipakai walau teks lama tanpa Direct Flight, asal Page sama dengan iklan di ad set & paketnya sama.**
- **Iklan mahal (21 Okt; diperbarui 30 Okt):** biaya per chat WA sepanjang tayang harus **di bawah Rp50rb** (30 Okt, perintah user "cpr harus di bawah 50rb") — iklan ACTIVE > Rp50rb/chat di-PAUSE berapa pun jumlah chatnya (pengecualian ≥5 chat dihapus); 0 chat dengan spend ≥ Rp35rb juga di-PAUSE. 30 Okt user minta "matikan" = PAUSE, bukan hapus.
- **Habiskan stok materi dulu (25 Okt, perintah user):** "habiskan dulu stok gambar dan video baru di pakai lagi" — saat mengisi banyak iklan, pakai setiap gambar/video dalam stok (folder materi paket itu) sekali dulu sebelum mengulang; bagi pemakaian merata (paling sedikit dipakai duluan). Stok Haji: 24 desain Haji Plus (Premium #1–8, Desain 3 #1–4, Desain 4 #1–4, Desain 6 #1–3, Desain 7 #1–2, Design 14 #1–3) + 18 video Hajj_2025-46..63 (library akun 947788760498911 / 1050343302646341). Desain 7 #3–#4 hanya di Canva (tool tak bisa unduh resolusi penuh).
- **Gambar unik antar ad set** dalam satu campaign — jangan duplikasi iklan/gambar yang sama persis (user menghapus yang kembar). Default isi ad set kosong: 3 iklan, gambar berbeda-beda.
- **CTA WhatsApp** (`WHATSAPP_MESSAGE`), link `https://api.whatsapp.com/send`.
- **Page** `588336968031663` (Elharamain wisata), **IG user** `17841405431328414`.
- **Nomor WhatsApp iklan per akun (22 Okt)** — iklan tiap akun memakai nomor sesuai nama akun, Page utama Elharamain wisata `588336968031663`:
  | Akun | No. WA |
  |---|---|
  | Fifi | 0812-8729-2422 |
  | AIni | 0851-7998-8198 |
  | Diana | 0856-9388-3208 |
  | Nida | 0812-1417-8056 |
  | Tira | 0813-2212-344 (memang 11 digit, dikonfirmasi user) |
  | Hanif | 0822-6012-6394 |
  | Fikri | 0858-4337-2026 |
  | Irfan | 0851-9938-1590 |
  | Alif / Allif | 0851-2631-4084 |
  **Phone number ID WhatsApp (22 Okt, dari WhatsApp Manager)** — dipakai di ad set `promoted_object.whats_app_business_phone_number_id`:
  Fikri 960847667109740 · Nida ("elharamain wisata jakarta") 965627883291461 · Diana 106153078857883 · Fifi (Profil Telepon) 103673662442851 · Hanif 737761806076654 · Alif 893984207120814 · AIni ("Elharamain Wisata Depok") 897107583479313 · Irfan 1049088094963016 · Tira: belum ada.
- **Headline** berselang-seling:
  - `7000+ Google Review ⭐️⭐️⭐️⭐️⭐️ (5.0)` (4 Nov: diganti dari 6800+, user: "untuk iklan baru ganti dari 6800 menjadi 7000 google review" + "maksudnya jika saya suruh lagi itu termasuk iklan baru" → BERLAKU untuk SEMUA iklan yang dibuat atas perintah berikutnya, semua akun Umroh & Haji; jangan pakai 6800+ lagi; 22 Okt: 6700+ → 6800+)
  - `✈️ Tiket Sudah Confirm, Jadwal Pasti`
- **Deskripsi:** `Hotel Bintang 5 · Seat terbatas 45/keberangkatan`
- **Cloudinary aktif (sejak 9 Okt, perintah user): cloud `q2xuhm0o`** — URL `https://res.cloudinary.com/q2xuhm0o/image/upload/<public_id>.jpg`. Cloud lama `v6gwkqrb` tidak dipakai lagi.
  Materi Ramadhan: `Elharamainwisata/ramadhan`. Materi Haji: 9 gambar di root cloud ini. (10 Okt) Desember, 9 Hari Januari, 12 Hari Januari sudah ada di cloud ini (`Elharamainwisata/Desember`, `/9 Hari Januari`, `/12 Hari Januari`). LAT & November belum ada — minta user upload dulu. (17 Okt) Desain baru: `9 Hari Januari` → Desain_7 #1–5 + Desain_4 Musim Dingin Premium #1–5; `12 Hari Januari` → Desain_2 12 Hari #1–5.
- **Canva (20 Okt):** akun Canva tersambung punya folder materi (isi = gambar upload, bukan desain): `9 Hari Januari` `FAHYiSew1AM` (35: **Desain 9 #1–5 baru (21 Okt)**, Desain 8 #1–4, Desain 3 #1–4, Desain 4 Januari #1–4, Desain 4 Musim Dingin Premium #1–5, Desain 7 #1–5, januari_1–8), `12 Hari Januari` `FAHYiWioa1g` (10: Desain 2 #1–5, 12_hari_januari_1–5), `Haji` `FAHYiYkarIo` (25: Desain 3 #1–4, Desain 4 #1–4, Desain 6 #1–3, Desain 7 #1–4, Desain Premium #1–8, Design 14 #1–2), `ramadhan` `FAHYiTALT_k` (11: Desain 2 #1–5, Desain 3 #1–6). **27 Okt:** ada salinan folder (dibuat 26 Okt 22:26): `9 Hari Januari` `FAHZH4MWBLA`, `ramadhan` `FAHZH7_sMDw`, `Copy of ramadhan`, `Copy of 12 Hari Januari`, `Copy of Haji` (24 gambar, termasuk Desain 7 #1–4), `Copy of Paket Umroh` (brosur PDF `UPDATE BROSUR JANUARI 2027` 13 hlm + `PAKET UMROH RAMADHAN 1448 H` 11 hlm) — isinya sama dengan folder asli, tidak ada desain baru.
- **Ambil gambar upload Canva resolusi penuh (27 Okt):** gambar upload di folder Canva hanya beri thumbnail, tapi bisa ditaruh ke desain lalu diekspor: `copy-design` desain 1080×1350 → `read-design open_transaction` → `add_page` 1080×1350 + `insert_fill` asset_id (top 0, left 0, 1080×1350) → commit → `export-design` jpg (quality 95). Desain kerja **`DAHZKazbAWs`** "Materi iklan export…": hlm 2–6 = Desain 9 Januari #1–5, hlm 7–8 = Haji Desain 7 #3–#4 (sudah diekspor 1080×1350, tajam). URL ekspor kedaluwarsa ±12 jam → ekspor ulang saat mau upload ke Meta (`ads_creative_upload_media` via URL). Tidak perlu Cloudinary.
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

- **Meta Ads DNA / Blueprint (22 Okt):** hasil skill Build DNA + Operating System ada di [`dna/`](dna/README.md). Untuk analisis/keputusan harian baca dulu Quick Reference Card di [`dna/05_BLUEPRINT_META_ADS_ELHARAMAIN_UMROH.md`](dna/05_BLUEPRINT_META_ADS_ELHARAMAIN_UMROH.md) (CPR baseline Rp27,9–39,3rb, safe Rp54,9rb, kill > Rp73,8rb, winner ≥5 chat & ≤ Rp39,3rb). Aturan user di file ini tetap menang.

## Catatan teknis Meta Ads MCP

- **Izin otomatis (11 Okt, perintah user "allow all"):** `.claude/settings.json` sekarang allow semua tool (seluruh Meta Ads, Cloudinary, Google Drive/Sheets, Canva, Elharamain, Bash, Read/Edit/Write, web). Berlaku mulai sesi baru. Aturan "iklan harus PAUSE" tetap: aktivasi/hapus hanya kalau user perintah eksplisit.

- **Akun Elharamain Haji (947788760498911):** Page iklan beda per kampanye — **tiru Page/IG dari iklan lama kampanye itu** (cek `ads_get_creatives` → `effective_object_story_id`). Kampanye **Irfan** pakai Page `588336968031663` + IG `17841405431328414` (bukan Page Haji `637020022834756`); Diana pakai Page Haji tanpa IG. Cara yang disukai user untuk kampanye Irfan: duplikat iklan yang ada lalu ganti gambar. Materi Haji di Cloudinary `Elharamainwisata/Haji` (gambar Desain/Premium + video Hajj_2025-46..63). **User minta iklan baru, jangan salin/pakai ulang iklan atau creative yang sudah ada** (5 Okt). Creative lama di akun ini terikat Page; creative Irfan tidak cocok untuk ad set lain.

- **Buat iklan massal (22 Okt):** akun draft bisa salin iklan dalam akun yang sama via `ads_create_ad` `source_ad_id` (lintas akun ditolak). `ads_create_ad` tidak menerima `status`; `ads_update_entity` hanya satu `entity_id` per panggilan dan wajib `ad_account_id`.
- `client_conversation_id` yang dipakai: `Hn4fT8qLz2WcP7xR1bVk` (`client_model`: `claude-sonnet-5-5`).
- **Jangan pernah pakai katalog (22 Okt, perintah user).** Campaign OUTCOME_SALES buatan API otomatis jadi `UNIFIED_SALES_PROXY` dengan toggle **Katalog Advantage+ menyala** → ad set WA kembali ke web & error. Tool tidak bisa mematikan toggle ini → minta user matikan manual di Ads Manager (atau user buat campaign Penjualan manual). Cara alternatif (22 Okt): buat campaign Penjualan dengan `source_campaign_id` campaign Sales buatan user (`120253855545180019` di AIni) + ad set `source_adset_id` — cek hasilnya di Ads Manager. Campaign Penjualan: `campaign_optimization_type: NONE`, tanpa product_set/catalog. Ad set Penjualan WA wajib kirim `conversion_locations: WHATSAPP` saat dibuat (kalau tidak, Ads Manager membacanya "Situs web & aplikasi" dan error peristiwa konversi).
- **Jangan publish kalau nomor WA belum dipasang (22 Okt):** nomor WA ad set tidak bisa diganti setelah terbit dan akun connector tidak punya akses aset nomor WA → biarkan campaign/ad set di DRAFT, user pasang nomor manual dulu.
- **Publish draft tapi tetap PAUSED (22 Okt, AIni):** user mau posisi "pause, bukan draf". Caranya: set campaign & iklan `status: PAUSED`, lalu `ads_activate_entity` dengan `object_ids` (campaign+ad set+iklan) dan `publish_as_active=false`. Kalau ad set error "You do not have access to the WhatsApp Business Phone Number", set `promoted_object` = `{"page_id":"588336968031663"}` saja (hapus whats_app_business_phone_number_id otomatis).
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

## Status per akun / Riyadh Air
- **Haji 2 (1032468828178224) SENGAJA DIMATIKAN SEMUA oleh user** (5 Nov: "haji 2 memang saya matikan semuanya tidak ada yang jalan"). Biaya Rp0 itu normal, bukan masalah. Jangan dinyalakan dan jangan dilaporkan sebagai masalah. Error 2446880 dari bot di Haji 2 = bot mencoba mem-pause iklan di akun yang memang sudah mati.

Riwayat lengkap per akun, ID campaign/ad set, dan tabel budget Haji dipindah ke [`arsip-status-akun.md`](arsip-status-akun.md) (2 Nov) agar bot Telegram lebih ringan.


- **Pindah akun Claude (1 Nov):** user akan pindah ke akun Claude Max (email beda). Langkah + isi lengkap 6 routine aktif ada di [`pindah-akun.md`](pindah-akun.md); setelah routine dibuat ulang di akun baru, matikan routine akun lama dan ganti ID `trig_…` di file ini.

- **Mac mini Ubuntu + Telegram (2 Nov):** langkah pasang Claude Code + repo + bot Telegram (`telegram/bot.py`, service `elharamain-bot`) di [`pindah-ubuntu.md`](pindah-ubuntu.md). Routine cloud tidak perlu dipindah. Token bot hanya di `telegram/.env` (tidak di-commit).

- **Rekap biaya bulanan semua platform** (Meta + Google Ads + TikTok Ads) di [`rekap-bulanan.md`](rekap-bulanan.md). Google Ads & TikTok Ads kena pajak 12% (Meta VAT 0%). Okt 2026: total Rp342,85 jt termasuk pajak.

## Pending / pertanyaan terbuka

- 27 Okt: akun IN_GRACE_PERIOD (pembayaran bermasalah) — Haji 3, AIni, Hanif, Fikri, Diana, Allif. Belanja 1–27 Okt semua akun ±Rp274 jt (rincian di chat-log).

- **28 Okt:** Elharamain Haji kembali ACTIVE (tagihan lunas), AIni ACTIVE; masih IN_GRACE_PERIOD: Fikri, Hanif, Diana, Allif, Haji 3.
- **27 Okt:** akun Elharamain Haji (947788760498911) UNSETTLED (tagihan belum lunas; level akun tak terbaca, tapi level campaign bisa: Rp37,73 jt/1.081 chat); Haji 3, AIni, Hanif, Fikri, Diana, Allif IN_GRACE_PERIOD. Rekap Okt (1–27): total ±Rp272,3 jt, 6.106 chat WA, Rp44.588/chat; sudah tertagih Meta 1–27 Okt Rp268,77 jt (belum tertagih terbesar: Hanif, Fikri, Diana, Allif, AIni) — detail di chat-log 27 Okt.

- 22 Okt: 4 campaign "(baru)" (Penjualan/Prospek/Interaksi/Traffic) × 3 ad set sudah ada di semua 9 akun Umroh (lihat chat-log 22 Okt "lanjut"). Belum ada iklan; nomor WA & toggle Katalog Advantage+ (Penjualan) dicek/diisi user.
- Diana: 5 ad set IG ARCHIVED — disengaja?
- Nida desember lama: 4 iklan — ditunda atas permintaan user.
- 8 Okt: user **menolak** pause lanjutan iklan Riyadh Air/November/LAT di Irfan (5 iklan LAT ad set `120253100040430414`) — jangan lanjutkan pause tanpa perintah baru.
- Template WA untuk iklan Ramadhan belum ditentukan.

