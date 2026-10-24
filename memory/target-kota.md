# Target kota default (aturan user 22 Okt 2026)

Sumber: ad set campaign **Sales** akun AIni (`814396810761205`), diatur manual oleh user.
Setiap iklan baru → lokasi ad set-nya disamakan dengan daftar ini (lihat aturan di `chat-memory.md`).

25 kota, radius **40 km**, + 5 subcity Jakarta. `location_types`: frequently_in, home, recent.

| Kota | Key | | Kota | Key |
|---|---|---|---|---|
| Jakarta | 962899 | | Balikpapan | 949414 |
| Bekasi | 951390 | | Banjarmasin | 950015 |
| Bandung | 949797 | | Bandar Lampung | 950016 |
| Bogor | 953142 | | Makassar | 973751 |
| Cibinong | 955404 | | Malang | 973850 |
| Depok | 957890 | | Medan | 975253 |
| Tangerang | 994587 | | Padang | 979675 |
| Serpong | 989923 | | Palembang | 980311 |
| Karawang | 966167 | | Pekanbaru | 982868 |
| Garut | 960633 | | Samarinda | 988013 |
| Cirebon | 956891 | | Semarang | 989399 |
| Sukabumi | 992117 | | Surakarta | 992961 |
| Tasikmalaya | 995230 | | | |

Subcity Jakarta: South 2727916, Central 2998930, East 2998931, North 2998932, West 2998933.

Kode lain (tidak dipakai di daftar): Cikarang 955995, Serang 989841, region Jakarta 1664.

## `geo_locations` siap pakai

```json
{"cities":[
 {"key":"962899","radius":40,"distance_unit":"kilometer"},
 {"key":"951390","radius":40,"distance_unit":"kilometer"},
 {"key":"949797","radius":40,"distance_unit":"kilometer"},
 {"key":"953142","radius":40,"distance_unit":"kilometer"},
 {"key":"955404","radius":40,"distance_unit":"kilometer"},
 {"key":"957890","radius":40,"distance_unit":"kilometer"},
 {"key":"994587","radius":40,"distance_unit":"kilometer"},
 {"key":"989923","radius":40,"distance_unit":"kilometer"},
 {"key":"966167","radius":40,"distance_unit":"kilometer"},
 {"key":"960633","radius":40,"distance_unit":"kilometer"},
 {"key":"956891","radius":40,"distance_unit":"kilometer"},
 {"key":"992117","radius":40,"distance_unit":"kilometer"},
 {"key":"995230","radius":40,"distance_unit":"kilometer"},
 {"key":"949414","radius":40,"distance_unit":"kilometer"},
 {"key":"950015","radius":40,"distance_unit":"kilometer"},
 {"key":"950016","radius":40,"distance_unit":"kilometer"},
 {"key":"973751","radius":40,"distance_unit":"kilometer"},
 {"key":"973850","radius":40,"distance_unit":"kilometer"},
 {"key":"975253","radius":40,"distance_unit":"kilometer"},
 {"key":"979675","radius":40,"distance_unit":"kilometer"},
 {"key":"980311","radius":40,"distance_unit":"kilometer"},
 {"key":"982868","radius":40,"distance_unit":"kilometer"},
 {"key":"988013","radius":40,"distance_unit":"kilometer"},
 {"key":"989399","radius":40,"distance_unit":"kilometer"},
 {"key":"992961","radius":40,"distance_unit":"kilometer"}],
 "subcities":[{"key":"2727916"},{"key":"2998930"},{"key":"2998931"},{"key":"2998932"},{"key":"2998933"}],
 "location_types":["frequently_in","home","recent"]}
```

Catatan: `targeting` di `ads_update_entity` mengganti seluruh targeting → ambil targeting ad set yang ada,
ganti hanya `geo_locations` (hapus `regions` jika ada), sisanya (umur, placement, `targeting_automation`) tetap.

## Penempatan default (aturan user 22 Okt 2026)

Semua Instagram + Facebook Story + WhatsApp Status + Threads:

```json
{"publisher_platforms":["facebook","instagram","whatsapp","threads"],
 "facebook_positions":["story"],
 "instagram_positions":["stream","story","explore_home","reels","profile_feed","ig_search","profile_reels"],
 "whatsapp_positions":["status"],
 "threads_positions":["threads_stream"],
 "device_platforms":["mobile","desktop"]}
```

Jangan pakai `explore` (error "IG Explore Placement Is Deprecated"); `explore_home` boleh.
Hapus `page_types`/`effective_*` saat mengirim targeting.

## Pembagian 5 kelompok wilayah (permintaan user 24 Okt 2026)

Dari 25 kota + 5 subcity Jakarta yang sedang berjalan (radius 40 km). Untuk ad set per wilayah,
pakai key kelompok itu saja di `geo_locations.cities` (radius 40 km; subcity Jakarta tanpa radius).

| Kelompok | Kota (key) | Jumlah |
|---|---|---|
| **Jakarta** | Jakarta 962899 + subcity South 2727916, Central 2998930, East 2998931, North 2998932, West 2998933 | 1 kota + 5 subcity |
| **Jawa Barat** | Bekasi 951390, Bandung 949797, Bogor 953142, Cibinong 955404, Depok 957890, Karawang 966167 (+ Karawang kedua 966166 di Fifi), Garut 960633, Cirebon 956891, Sukabumi 992117, Tasikmalaya 995230, **Cikarang 955995** | 11 |
| **Banten** | Tangerang 994587, Serpong 989923, **Serang 989841**, **Cilegon 956300**, **Balaraja 949353** | 5 |
| **Pulau Jawa** (Jateng & Jatim) | Semarang 989399, Surakarta 992961, Malang 973850 | 3 |
| **Luar Pulau Jawa** | Medan 975253, Padang 979675, Pekanbaru 982868, Palembang 980311, Bandar Lampung 950016, Balikpapan 949414, Samarinda 988013, Banjarmasin 950015, Makassar 973751 | 9 |

Catatan: radius 40 km dari Jakarta ikut menjangkau Tangerang, Depok, dan Bekasi. Kalau ad set per wilayah
jalan bersamaan, audiens Jakarta–Jabar–Banten bisa tumpang tindih. Kota tambahan (Serang, Cilegon, Balaraja,
Cikarang, Karawang 966166) ditambahkan manual oleh user di Fifi campaign **Banten** (`120252597264440365` Ramadhan,
`…263870365` 9 Hari Januari, `…264430365` 12 Hari Januari, ACTIVE) → di sana total 30 kota radius 40 km + 5 subcity.
Belum jadi default akun lain sampai user perintah.

## Akun Haji (1050343302646341) — 5 wilayah per campaign (24 Okt 2026)

Setiap campaign Haji punya 5 ad set: Jakarta, Jawa Barat, Banten, Jawa, Luar Pulau (kota sama seperti tabel di atas, radius 40 km).
**Khusus Haji, Jawa = Semarang 989399, Surakarta 992961, Malang 973850 + Surabaya 992951** (key Surabaya dari ad set yang diisi manual user).
Umur Haji 30–50 dengan `targeting_automation.individual_setting.age=0`.
