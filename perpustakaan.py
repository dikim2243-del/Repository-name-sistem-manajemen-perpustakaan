import csv
import os
from collections import deque

FILE_BUKU = "buku.csv"

antrian = deque()

# ==========================
# DATABASE CSV
# ==========================

def buat_file():
    if not os.path.exists(FILE_BUKU):
        with open(FILE_BUKU, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["kode", "judul", "penulis", "stok"])


def baca_buku():
    data = {}

    with open(FILE_BUKU, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data[row["kode"]] = {
                "judul": row["judul"],
                "penulis": row["penulis"],
                "stok": int(row["stok"])
            }

    return data


def simpan_buku(data):
    with open(FILE_BUKU, mode="w", newline="") as file:
        fieldnames = ["kode", "judul", "penulis", "stok"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for kode, buku in data.items():
            writer.writerow({
                "kode": kode,
                "judul": buku["judul"],
                "penulis": buku["penulis"],
                "stok": buku["stok"]
            })


# ==========================
# CREATE
# ==========================

def tambah_buku():
    data = baca_buku()

    kode = input("Kode Buku : ")

    if kode in data:
        print("Kode sudah digunakan!")
        return

    judul = input("Judul Buku : ")
    penulis = input("Penulis : ")
    stok = int(input("Stok : "))

    data[kode] = {
        "judul": judul,
        "penulis": penulis,
        "stok": stok
    }

    simpan_buku(data)

    print("Buku berhasil ditambahkan!")


# ==========================
# READ
# ==========================

def lihat_buku():
    data = baca_buku()

    if len(data) == 0:
        print("Belum ada data buku")
        return

    print("\n===== DAFTAR BUKU =====")

    for kode, buku in data.items():
        print(
            f"{kode} | "
            f"{buku['judul']} | "
            f"{buku['penulis']} | "
            f"Stok: {buku['stok']}"
        )


# ==========================
# UPDATE
# ==========================

def update_buku():
    data = baca_buku()

    kode = input("Masukkan kode buku: ")

    if kode not in data:
        print("Buku tidak ditemukan")
        return

    judul = input("Judul baru : ")
    penulis = input("Penulis baru : ")
    stok = int(input("Stok baru : "))

    data[kode] = {
        "judul": judul,
        "penulis": penulis,
        "stok": stok
    }

    simpan_buku(data)

    print("Data berhasil diperbarui")


# ==========================
# DELETE
# ==========================

def hapus_buku():
    data = baca_buku()

    kode = input("Masukkan kode buku: ")

    if kode not in data:
        print("Buku tidak ditemukan")
        return

    del data[kode]

    simpan_buku(data)

    print("Buku berhasil dihapus")


# ==========================
# SEARCHING
# ==========================

def cari_buku():
    data = baca_buku()

    keyword = input("Cari judul buku : ").lower()

    ditemukan = False

    for kode, buku in data.items():
        if keyword in buku["judul"].lower():
            print(
                f"{kode} | "
                f"{buku['judul']} | "
                f"{buku['penulis']} | "
                f"Stok: {buku['stok']}"
            )

            ditemukan = True

    if not ditemukan:
        print("Buku tidak ditemukan")


# ==========================
# SORTING
# ==========================

def urutkan_buku():
    data = baca_buku()

    hasil = sorted(
        data.items(),
        key=lambda x: x[1]["judul"]
    )

    print("\n===== DATA TERURUT =====")

    for kode, buku in hasil:
        print(
            f"{kode} | "
            f"{buku['judul']} | "
            f"{buku['penulis']} | "
            f"Stok: {buku['stok']}"
        )


# ==========================
# QUEUE PEMINJAMAN
# ==========================

def tambah_antrian():
    nama = input("Nama peminjam : ")

    antrian.append(nama)

    print("Masuk antrian peminjaman")


def layani_peminjam():
    if len(antrian) == 0:
        print("Antrian kosong")
        return

    nama = antrian.popleft()

    print(f"Peminjam {nama} telah dilayani")


def lihat_antrian():
    if len(antrian) == 0:
        print("Antrian kosong")
        return

    print("\n===== ANTRIAN PEMINJAMAN =====")

    nomor = 1

    for orang in antrian:
        print(f"{nomor}. {orang}")
        nomor += 1


# ==========================
# MENU
# ==========================

def menu():

    while True:

        print("\n")
        print("=" * 40)
        print("SISTEM MANAJEMEN PERPUSTAKAAN")
        print("=" * 40)

        print("1. Tambah Buku")
        print("2. Lihat Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Cari Buku")
        print("6. Urutkan Buku")
        print("7. Tambah Antrian")
        print("8. Layani Peminjam")
        print("9. Lihat Antrian")
        print("10. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            tambah_buku()

        elif pilihan == "2":
            lihat_buku()

        elif pilihan == "3":
            update_buku()

        elif pilihan == "4":
            hapus_buku()

        elif pilihan == "5":
            cari_buku()

        elif pilihan == "6":
            urutkan_buku()

        elif pilihan == "7":
            tambah_antrian()

        elif pilihan == "8":
            layani_peminjam()

        elif pilihan == "9":
            lihat_antrian()

        elif pilihan == "10":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak tersedia")


buat_file()
menu()