# Sistem Manajemen Perpustakaan

## Deskripsi

Sistem Manajemen Perpustakaan merupakan aplikasi berbasis Python yang digunakan untuk mengelola data buku menggunakan database CSV. Program ini dapat melakukan operasi CRUD (Create, Read, Update, Delete), pencarian data, pengurutan data, serta pengelolaan antrian peminjam.

## Fitur

* Tambah Data Buku
* Lihat Data Buku
* Update Data Buku
* Hapus Data Buku
* Cari Buku
* Urutkan Buku Berdasarkan Judul
* Tambah Antrian Peminjam
* Layani Peminjam
* Lihat Antrian Peminjam

## Struktur Data yang Digunakan

1. Dictionary (Hash Map)

   * Digunakan untuk menyimpan data buku berdasarkan kode buku.

2. Queue (Antrian)

   * Digunakan untuk mengelola antrian peminjam dengan metode FIFO (First In First Out).

## Teknologi yang Digunakan

* Python
* CSV (Flat File Database)

## Struktur File

```
PERPUSTAKAAN/
│
├── perpustakaan.py
└── buku.csv
```

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Buka terminal pada folder proyek.
3. Jalankan perintah:

```bash
python perpustakaan.py
```

## Menu Program

1. Tambah Buku
2. Lihat Buku
3. Update Buku
4. Hapus Buku
5. Cari Buku
6. Urutkan Buku
7. Tambah Antrian
8. Layani Peminjam
9. Lihat Antrian
10. Keluar

## Penulis

Muhammad Diki

Proyek UAS Struktur Data - Sistem Manajemen Perpustakaan
