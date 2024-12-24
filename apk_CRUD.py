import mysql.connector
from rich.align import Align
from rich.console import Console
from rich.text import Text
from tabulate import tabulate
from datetime import datetime  
import pyfiglet  
import time  

console = Console()

connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="",
    database="restaurant",
)

def display_banner():
    banner = pyfiglet.figlet_format("Restaurant Serba Bisa", font="slant")
    console.print(Align.center(banner))

def main(connection):
    print("Loading, please wait...")  
    time.sleep(2)  
    display_banner() 
    while True:
        main_menu_data = [
            ["1", "Manajemen Menu"],
            ["2", "Manajemen Pelanggan"], 
            ["3", "Manajemen Pemesanan"], 
            ["4", "Keluar"]
        ]
        main_menu_box = tabulate(main_menu_data, headers=["No", "Menu"], tablefmt="fancy_grid")
        console.print(Align.center(main_menu_box))
        choice = input(" "*125 + "Pilih menu: ")
        if choice == "1":
            manajemen_menu(connection)
        elif choice == "2":
            manajemen_pelanggan(connection)  
        elif choice == "3":
            manajemen_pemesanan(connection)  
        elif choice == "4":
            print("Loading, please wait...")  
            time.sleep(2)  
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

def manajemen_pelanggan(connection):
    while True:
        pelanggan_data = [
            ["1", "Tambah Pelanggan"],
            ["2", "Lihat Pelanggan"],
            ["3", "Update Pelanggan"],
            ["4", "Hapus Pelanggan"],
            ["5", "Kembali ke Menu Utama"]
        ]
        pelanggan_box = tabulate(pelanggan_data, headers=["No", "Menu"], tablefmt="fancy_grid")
        console.print(Align.center(pelanggan_box))
        choice = input(" "*125 + "Pilih menu: ")
        if choice == "1":
            tambah_pelanggan(connection)
        elif choice == "2":
            lihat_pelanggan(connection)
        elif choice == "3":
            ubah_pelanggan(connection)
        elif choice == "4":
            hapus_pelanggan(connection)
        elif choice == "5":
            break
        else:
            console.print(Align.center("Pilihan tidak valid!"))


def tambah_pelanggan(connection):
    cursor = connection.cursor()
    nama = input(" "*117+"Masukkan nama pelanggan: ")
    nomor_telepon = input(" "*117+"Masukkan nomor telepon pelanggan: ")
    cursor.execute(
        "INSERT INTO pelanggan (nama, nomor_telepon) VALUES (%s, %s)",
        (nama, nomor_telepon),
    )
    connection.commit()
    cursor.close()
    print("Pelanggan berhasil ditambahkan!")

def lihat_pelanggan(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pelanggan")
    pelanggan = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    cursor.close()

    console.print(Align.center("\nDaftar Pelanggan:"))
    console.print(Align.center(tabulate(pelanggan, headers=headers, tablefmt="fancy_grid")))


def ubah_pelanggan(connection):
    lihat_pelanggan(connection)
    id_pelanggan = int(input(" "*117+"Masukkan ID pelanggan yang akan diupdate: "))
    nama_baru = input(" "*117+"Masukkan nama pelanggan baru: ")
    nomor_telepon_baru = input(" "*117+"Masukkan nomor telepon baru: ")

    cursor = connection.cursor()
    cursor.execute(
        "UPDATE pelanggan SET nama = %s, nomor_telepon = %s WHERE id_pelanggan = %s",
        (nama_baru, nomor_telepon_baru, id_pelanggan),
    )
    connection.commit()
    cursor.close()
    console.print(Align.center("Pelanggan berhasil diupdate!"))

def hapus_pelanggan(connection):
    lihat_pelanggan(connection)
    id_pelanggan = int(input(" "*117+"Masukkan ID pelanggan yang akan dihapus: "))

    cursor = connection.cursor()
    cursor.execute("DELETE FROM pelanggan WHERE id_pelanggan = %s", (id_pelanggan,))
    connection.commit()
    cursor.close()
    console.print(Align.center("Pelanggan berhasil dihapus!"))

def manajemen_menu(connection):
    while True:
        menu_data = [
            ["1", "Tambah Menu"],
            ["2", "Lihat Menu"],
            ["3", "Update Menu"],
            ["4", "Hapus Menu"],
            ["5", "Kembali ke Menu Utama"]
        ]
        menu_box = tabulate(menu_data, headers=["No", "Menu"], tablefmt="fancy_grid")
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
            console.print(Align.center("Pilihan tidak valid!"))

def tambah_menu(connection):
    nama_menu = input(" "*117+"Masukkan nama menu: ")
    print(" "*117+"(Makanan/Minuman)")
    kategori = input(""*117+"Masukkan kategori: ")
    harga = float(input(""*117+"Masukkan harga    : "))

    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Menu (nama_menu, kategori, harga) VALUES (%s, %s, %s)",
        (nama_menu, kategori, harga),
    )
    connection.commit()
    cursor.close()
    console.print(Align.center("Menu berhasil ditambahkan!"))

def lihat_menu(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Menu")
    menus = cursor.fetchall()
    cursor.close()

    headers = [desc[0] for desc in cursor.description]
    console.print(Align.center("\nDaftar Menu:"))
    console.print(Align.center(tabulate(menus, headers=headers, tablefmt="fancy_grid")))

def ubah_menu(connection):
    lihat_menu(connection)
    id_menu = int(input(" "*117+"Masukkan ID menu yang akan diupdate: "))
    nama_menu = input(" "*117+"Masukkan nama menu baru: ")
    kategori = input(" "*117+"Masukkan kategori baru : ")
    harga = float(input(" "*117+"Masukkan harga baru: "))

    cursor = connection.cursor()
    cursor.execute(
        "UPDATE Menu SET nama_menu = %s, kategori = %s, harga = %s WHERE id_menu = %s",
        (nama_menu, kategori, harga, id_menu),
    )
    connection.commit()
    cursor.close()
    console.print(Align.center("Menu berhasil diupdate!"))

def hapus_menu(connection):
    lihat_menu(connection)
    id_menu = int(input(" "*117+"Masukkan ID menu yang akan dihapus: "))

    cursor = connection.cursor()
    cursor.execute("DELETE FROM Menu WHERE id_menu = %s", (id_menu,))
    connection.commit()
    cursor.close()
    console.print(Align.center("Menu berhasil dihapus!"))

def manajemen_pemesanan(connection):
    while True:
        pemesanan_data = [
            ["1", "Tambah Pemesanan"],
            ["2", "Lihat Pemesanan"],
            ["3", "Cetak Struk"],
            ["4", "Kembali ke Menu Utama"]
        ]
        pemesanan_box = tabulate(pemesanan_data, headers=["No", "Menu"], tablefmt="fancy_grid")
        console.print(Align.center(pemesanan_box))
        choice = input(" "*125 + "Pilih menu: ")
        if choice == "1":
            tambah_pesanan(connection)
        elif choice == "2":
            lihat_pemesanan(connection)
        elif choice == "3":
            detail_pemesanan(connection)
        elif choice == "4":
            break
        else:
            console.print(Align.center("Pilihan tidak valid!"))

from datetime import datetime
from rich.console import Console
from rich.align import Align

console = Console()

from datetime import datetime
from rich.console import Console
from rich.align import Align

console = Console()

def tambah_pesanan(connection):
    lihat_pelanggan(connection)
    try:
        id_pelanggan = int(input(" "*117+"Masukkan Id pelanggan: "))
        tanggal_pemesanan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO pemesanan (id_pelanggan, tanggal_pemesanan, total_harga) VALUES (%s, %s, 0)",
            (id_pelanggan, tanggal_pemesanan),
        )
        id_pemesanan = cursor.lastrowid

        total_harga = 0
        while True:
            lihat_menu(connection)
            id_menu = int(input(" "*117+"Masukkan ID menu: "))
            jumlah = int(input(" "*117+"Masukkan jumlah: "))

            
            cursor.execute("SELECT harga FROM menu WHERE id_menu = %s", (id_menu,))
            harga_data = cursor.fetchone()
            if not harga_data:
                console.print(Align.center("[red]Menu tidak ditemukan![/red]")) 
                continue
            harga = harga_data[0]

            
            subtotal = harga * jumlah
            total_harga += subtotal

            
            cursor.execute(
                "INSERT INTO detailpemesanan (id_pemesanan, id_menu, jumlah, subtotal) VALUES (%s, %s, %s, %s)",
                (id_pemesanan, id_menu, jumlah, subtotal),
            )

            tambah_lagi = input(" "*117+"Tambah menu lain (y/n): ").lower()
            if tambah_lagi != "y":
                break

        
        cursor.execute(
            "UPDATE pemesanan SET total_harga = %s WHERE id_pemesanan = %s",
            (total_harga, id_pemesanan),
        )

        connection.commit()
        console.print(Align.center("[green]Pemesanan berhasil ditambahkan![/green]"))
        console.print(Align.center(f"[green]Tanggal Pemesanan: {tanggal_pemesanan}[/green]")) 
    except Exception as e:
        console.print(f"[red]Terjadi kesalahan: {e}[/red]")
        connection.rollback()
    finally:
        if 'cursor' in locals():
            cursor.close()

def lihat_pemesanan(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT p.id_pemesanan, pl.nama, p.tanggal_pemesanan, p.total_harga FROM pemesanan p JOIN pelanggan pl ON p.id_pelanggan = pl.id_pelanggan")

    pemesanan = cursor.fetchall()

    table_data = []
    for pesan in pemesanan:
        table_data.append([pesan[0], pesan[1], pesan[2], pesan[3]])

    headers = ["id_pemesanan", "id_pelanggan", "tanggal_pemesanan", "total_harga"]
    console.print(Align.center("\nDaftar Pemesanan:"))
    console.print(Align.center(tabulate(table_data, headers=headers, tablefmt="fancy_grid")))

def detail_pemesanan(connection):
    lihat_pemesanan(connection)
    id_pemesanan = int(input(" "*110+"Masukkan id_pemesanan untuk melihat detail: "))

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT p.id_pemesanan, pl.nama, p.tanggal_pemesanan, p.total_harga
        FROM Pemesanan p
        JOIN Pelanggan pl ON p.id_pelanggan = pl.id_pelanggan
        WHERE p.id_pemesanan = %s
        """,
        (id_pemesanan,),
    )
    pemesanan = cursor.fetchone()

    if not pemesanan:
        console.print("[red]id pemesanan tidak ditemukan.[/red]")
        return

    cursor.execute(
        """
        SELECT m.nama_menu, dp.jumlah, dp.subtotal
        FROM DetailPemesanan dp
        JOIN Menu m ON dp.id_menu = m.id_menu
        WHERE dp.id_pemesanan = %s
        """,
        (id_pemesanan,),
    )
    detail = cursor.fetchall()
    cursor.close()

    console.print("\n" + "=" * 40, justify="center")
    console.print("SERBA", justify="center")
    console.print("=" * 40, justify="center")

    console.print(" " *113+f"id_pemesanan   : {pemesanan[0]}")
    console.print(" " *113+f"Nama Pelanggan : {pemesanan[1]}")
    console.print(" " *113+f"Tanggal        : {pemesanan[2]}")
    
    console.print("-" * 40, justify="center")
    console.print(f"{'Menu':<20}{'Qty':<5}{'Subtotal':>10}", justify="center")
    console.print("-" * 40, justify="center")

    for item in detail:
        menu_line = f"{item[0]:<20}{item[1]:<5}{item[2]:>10,.2f}"
        console.print(Align.center(Text(menu_line, justify="left")))

    console.print("-" * 40, justify="center")
    total_line = f"{'Total Harga':<25}{pemesanan[3]:>10,.2f}"
    console.print(Align.center(Text(total_line, justify="left")))
    console.print("=" * 40, justify="center")

if __name__ == "__main__":
    main(connection)