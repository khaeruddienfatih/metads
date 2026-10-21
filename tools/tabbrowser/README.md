# TabBrowser

Browser sederhana (Electron): setiap tab punya cookies/sesi sendiri, seperti membuka browser baru.
Cookies tab hilang saat tab ditutup.

- Tab baru: tombol `+` atau `Ctrl+T`. Tutup tab: `×` atau `Ctrl+W`.
- Link yang membuka jendela baru akan dibuka di tab yang sama (memakai cookies tab itu).

## Build `.exe` Windows

```
npm i -D electron@38.8.6 @electron/packager@20.3.0
npx electron-packager . TabBrowser --platform=win32 --arch=x64 --out=dist --overwrite --ignore=node_modules
```

Hasilnya ada di folder `dist/TabBrowser-win32-x64/TabBrowser.exe`. Bagikan seluruh folder itu (bisa di-zip).
