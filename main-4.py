# Variabel global untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambahkan mahasiswa
def create_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    data_mahasiswa.append(nama)
    print(f"Mahasiswa '{nama}' berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua mahasiswa
def read_mahasiswa():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.\n")
    else:
        print("Data Mahasiswa:")
        for i, nama in enumerate(data_mahasiswa):
            print(f"{i}. {nama}")
        print()

# Fungsi untuk mengubah nama mahasiswa
def update_mahasiswa():
    read_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin diubah: "))
        if 0 <= indeks < len(data_mahasiswa):
            nama_baru = input("Masukkan nama baru: ")
            data_lama = data_mahasiswa[indeks]
            data_mahasiswa[indeks] = nama_baru
            print(f"Mahasiswa '{data_lama}' berhasil diubah menjadi '{nama_baru}'.\n")
        else:
            print("Indeks tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka.\n")

# Fungsi untuk menghapus mahasiswa
def delete_mahasiswa():
    read_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin dihapus: "))
        if 0 <= indeks < len(data_mahasiswa):
            nama = data_mahasiswa.pop(indeks)
            print(f"Mahasiswa '{nama}' berhasil dihapus.\n")
        else:
            print("Indeks tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka.\n")

# Fungsi utama
def main():
    while True:
        print("=== Menu Manajemen Mahasiswa ===")
        print("1. Tambah Mahasiswa (Create)")
        print("2. Tampilkan Mahasiswa (Read)")
        print("3. Ubah Mahasiswa (Update)")
        print("4. Hapus Mahasiswa (Delete)")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            create_mahasiswa()
        elif pilihan == '2':
            read_mahasiswa()
        elif pilihan == '3':
            update_mahasiswa()
        elif pilihan == '4':
            delete_mahasiswa()
        elif pilihan == '5':
            print("Terima kasih. Program selesai.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Menjalankan program
if __name__ == "__main__":
    main()