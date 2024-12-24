import mysql.connector

connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="",
    database="restaurant",
)

cursor = connection.cursor()
query = """CREATE TABLE IF NOT EXISTS Pemesanan (
        id_pemesanan INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pelanggan INTEGER NOT NULL,
        tanggal_pemesanan TEXT NOT NULL,
        total_harga REAL NOT NULL,
        FOREIGN KEY (id_pelanggan) REFERENCES Pelanggan (id_pelanggan))"""

cursor.execute(query)
print("Tabel Pemesanan Berhasil Dibuat")

cursor.execute("show tables")
print(cursor.fetchall())

print()

cursor.execute("DESC Pemesanan")
result = cursor.fetchall()
for row in result:
    print(row)