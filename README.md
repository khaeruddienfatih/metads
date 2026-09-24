# metads — Otomatisasi Iklan Meta dari Cloudinary

Script ini membaca file config YAML dan mengambil gambar/video dari folder atau tag Cloudinary. Setelah itu script membuat
**Campaign → Ad Set → Creative → Ad** di Meta. **Semua objek dibuat dalam status PAUSED**, jadi Anda
review dulu di Ads Manager sebelum mengaktifkannya.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # isi token Meta + kredensial Cloudinary
```

- `META_ACCESS_TOKEN`: token System User (Business Manager) dengan izin `ads_management` dan `pages_read_engagement`.
- `META_AD_ACCOUNT_ID`: format `act_123...`.
- `CLOUDINARY_*`: dari Cloudinary → Settings → API Keys.

## Pemakaian

```bash
# 1. Dry-run: lihat apa yang akan dibuat (tidak mengubah apa pun di Meta)
python -m metads config/umroh-premium-1448.yaml

# 2. Buat beneran (semua PAUSED)
python -m metads config/umroh-premium-1448.yaml --apply
```

## Alur kerja harian

1. Upload creative baru (gambar/video) ke folder Cloudinary yang ada di config, misalnya `Elharamainwisata/Umroh/desember`.
2. Jalankan `--apply`. Script hanya membuat iklan untuk **aset baru**, karena aset lama sudah tercatat di `state/<name>.json`.
3. Review di Ads Manager, lalu aktifkan.

Satu iklan dibuat untuk setiap kombinasi **aset × copy**. Kalau ada 5 gambar dan 2 copy, hasilnya 10 iklan.
Setiap ad set dibatasi maksimal 50 iklan.

## Config

Lihat `config/umroh-premium-1448.yaml` sebagai template. Poin penting:

| Field | Keterangan |
|---|---|
| `name` | Kunci unik; menentukan file state. Ganti kalau mau campaign baru. |
| `campaign.daily_budget` | Isi untuk CBO. Kalau kosong, isi `daily_budget` di tiap ad set. |
| `daily_budget` | Untuk IDR tulis rupiah langsung (mis. `150000`). |
| `source.folder` / `source.tag` | Sumber aset di Cloudinary (fixed dan dynamic folder didukung). |
| `copies` | Daftar variasi `primary_text`, `headline`, `description`. Pakai `headlines: [a, b]` untuk test beberapa judul dengan copy yang sama. |
| `call_to_action` | `LEARN_MORE`, `SHOP_NOW`, `SIGN_UP`, `CONTACT_US`, `WHATSAPP_MESSAGE`, dll. |

Kalau proses gagal di tengah jalan, jalankan ulang saja. Objek yang sudah dibuat tidak akan diduplikasi.

## Test

```bash
pip install pytest && python -m pytest -q
```
