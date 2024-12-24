import mysql.connector
from rich.align import Align
from rich.console import Console
console = Console()

connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "",
    database = "restaurant",
)


# CRUD Functions for Menu
def manajemen_menu(connection):
    while True:
        menu_box = (
        "\n╔══════════════════════════════════╗\n"
        "║          Manajemen Menu          ║\n"
        "╠══════════════════════════════════╣\n"
        "║ 1. Tambah Menu                   ║\n"
        "║ 2. Lihat Menu                    ║\n"
        "║ 3. Update Menu                   ║\n"
        "║ 4. Hapus Menu                    ║\n"
        "║ 5. Kembali ke Menu Utama         ║\n"
        "╚══════════════════════════════════╝"
    )
        console.print(Align.center(menu_box))
        choice = input(" "*125+"Pilih menu: ")
        if choice == "1":
            tambah_menu(connection)
        elif choice == "2":
            lihat_menu(connection)
        elif choice == "3":
            ubah_menu(connection)
        elif choice == "4":
            hapus_menu(connection)
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid!")

def tambah_menu(connection):
    nama_menu = input("Masukkan nama menu: ")
    kategori = input("Masukkan kategori (Makanan/Minuman): ")
    harga = float(input("Masukkan harga: "))

    cursor = connection.cursor()
    cursor.execute("INSERT INTO Menu (nama_menu, kategori, harga) VALUES (%s, %s, %s)", (nama_menu, kategori, harga))
    cursor.commit()
    cursor.close()
    print("Menu berhasil ditambahkan!")

def lihat_menu(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Menu")
    menus = cursor.fetchall()
    cursor.close()

    print("\nDaftar Menu:")
    for menu in menus:
        print(menu)

def ubah_menu(connection):
    lihat_menu(connection)
    id_menu = int(input("Masukkan ID menu yang akan diupdate: "))
    nama_menu = input("Masukkan nama menu baru: ")
    kategori = input("Masukkan kategori baru: ")
    harga = float(input("Masukkan harga baru: "))

    
    cursor = connection.cursor()
    cursor.execute("UPDATE Menu SET nama_menu = %s, kategori = %s, harga = %s WHERE id_menu = %s", (nama_menu, kategori, harga, id_menu))
    cursor.commit()
    cursor.close()
    print("Menu berhasil diupdate!")

def hapus_menu(connection):
    lihat_menu(connection)
    id_menu = int(input("Masukkan ID menu yang akan dihapus: "))

    cursor = connection.cursor()
    cursor.execute("DELETE FROM Menu WHERE id_menu = %s", (id_menu,))
    cursor.commit()
    cursor.close()
    print("Menu berhasil dihapus!")

# CRUD Functions for Pemesanan and DetailPemesanan
def tambah_pesanan(connection):
    view_pelanggan(connection)
    id_pelanggan = int(input("Masukkan ID pelanggan: "))
    tanggal_pemesanan = input("Masukkan tanggal pemesanan (YYYY-MM-DD): ")

    
    cursor = connection.cursor()

    # Add Pemesanan
    cursor.execute("INSERT INTO Pemesanan (id_pelanggan, tanggal_pemesanan, total_harga) VALUES (%s, %s, 0)", (id_pelanggan, tanggal_pemesanan))
    id_pemesanan = cursor.lastrowid

    # Add DetailPemesanan
    total_harga = 0
    while True:
        lihat_menu(connection)
        id_menu = int(input("Masukkan ID menu: "))
        jumlah = int(input("Masukkan jumlah: "))
        cursor.execute("SELECT harga FROM Menu WHERE id_menu = %s", (id_menu,))
        harga = cursor.fetchone()[0]
        subtotal = harga * jumlah
        total_harga += subtotal

        cursor.execute("INSERT INTO DetailPemesanan (id_pemesanan, id_menu, jumlah, subtotal) VALUES (%s, %s, %s, %s)", (id_pemesanan, id_menu, jumlah, subtotal))

        tambah_lagi = input("Tambah menu lain%s (y/n): ").lower()
        if tambah_lagi != 'y':
            break

    # Update total harga di tabel Pemesanan
    cursor.execute("UPDATE Pemesanan SET total_harga = %s WHERE id_pemesanan = %s", (total_harga, id_pemesanan))

    cursor.commit()
    cursor.close()
    print("Pemesanan berhasil ditambahkan!")

def lihat_pemesanan(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Pemesanan")
    pemesanan = cursor.fetchall()
    cursor.close()

    print("\nDaftar Pemesanan:")
    for pesan in pemesanan:
        print(pesan)

# Functions to view Pelanggan
def view_pelanggan(connection):   
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Pelanggan")
    pelanggan = cursor.fetchall()
    cursor.close()

    print("\nDaftar Pelanggan:")
    for p in pelanggan:
        print(p)

# Main Menu
def main(connection):
    while True:
        menu_box = (
        "\n╔══════════════════════════════════╗\n"
        "║         Manajemen Restoran       ║\n"
        "╠══════════════════════════════════╣\n"
        "║ 1. Manajemen Menu                ║\n"
        "║ 2. Tambah Pemesanan              ║\n"
        "║ 3. Lihat Pemesanan               ║\n"
        "║ 4. Keluar                        ║\n"
        "╚══════════════════════════════════╝"
    )
        console.print(Align.center(menu_box))
        choice = input(" "*125+"Pilih menu: ")
        if choice == "1":
            manajemen_menu(connection)
        elif choice == "2":
            tambah_pesanan(connection)
        elif choice == "3":
            lihat_pemesanan(connection)
        elif choice == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main(connection)
