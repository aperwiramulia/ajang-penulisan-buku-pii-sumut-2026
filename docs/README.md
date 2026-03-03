# Ajang Penulisan Buku PII Sumut 2026 Website

Situs statis sederhana berisi informasi dari dokumen PDF di folder induk.

## Struktur

```
website/
  index.html        # halaman utama
  css/styles.css    # gaya
  img/flyer.jpeg    # flyer acara
  docs/             # salinan file PDF untuk diunduh
    *.pdf
```

## Menjalankan server lokal

1. Buka PowerShell dan navigasi ke folder `website`.
2. Jalankan `python -m http.server 8000`.
3. Bukalah `http://localhost:8000` di peramban untuk melihat situs.

## Mengedit konten

- Teks dasar diambil dari file `*.txt` yang diekstrak dari PDF.
- Ubah `index.html` jika perlu memoles bahasa atau menambahkan bagian.

## Catatan

Dokumen PDF asli dan teks yang diekstrak tersedia di folder atas; unduhan ditautkan di halaman.
