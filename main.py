from books.book import Book
import json

def tambah_buku(judul, pengarang, tahun_terbit):
    # Membuat objek buku baru
    buku_baru = Book(judul, pengarang, tahun_terbit)
    
    # Membuka file JSON
    # r untuk read
    with open("data/books.json", "r") as file:
        data = json.load(file)
        
    # Menambahkan buku ke dalam data
    data.append({
        "title": buku_baru.title,
        "author": buku_baru.author,
        "year": buku_baru.year
    })
    
    # fungsi json dump untuk menulis ulang kembali data yang diperbaharui ke dalam file JSON
    # w untuk write
    with open("data/books.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print("Buku berhasil ditambahkan.")
    print()

def cari_buku(judul):
    # Membuka file JSON
    with open("data/books.json", "r") as file:
        data = json.load(file)
        
    # Mencari buku berdasarkan judul (perhatikan besar kecilnya huruf)
    for buku in data:
        if buku["title"] == judul:
            print()
            print("Buku ditemukan:")
            print(f"Judul: {buku['title']}")
            print(f"Pengarang: {buku['author']}")
            print(f"Tahun Terbit: {buku['year']}")
            print()
            return
    
    print("Buku tidak ditemukan.")

def tampilkan_daftar_buku():
    # Membuka file JSON
    with open("data/books.json", "r") as file:
        data = json.load(file)
        
    print()
    print("Daftar Buku:")
    print()
    for buku in data:
        print(f"Judul: {buku['title']}")
        print(f"Pengarang: {buku['author']}")
        print(f"Tahun Terbit: {buku['year']}")
        print()

if __name__ == "__main__":
    while True:
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Tampilkan Daftar Buku")
        print("4. Keluar")
        print()
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan nama pengarang: ")
            tahun_terbit = int(input("Masukkan tahun terbit: "))
            tambah_buku(judul, pengarang, tahun_terbit)
        elif pilihan == "2":
            judul = input("Masukkan judul buku yang ingin dicari: ")
            cari_buku(judul)
        elif pilihan == "3":
            tampilkan_daftar_buku()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
