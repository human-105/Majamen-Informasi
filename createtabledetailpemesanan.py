import mysql.connector

connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="",
    database="restaurant",
)

cursor = connection.cursor()
query = """'CREATE TABLE IF NOT EXISTS DetailPemesanan (
        id_detail INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pemesanan INTEGER NOT NULL,
        id_menu INTEGER NOT NULL,
        jumlah INTEGER NOT NULL,
        subtotal REAL NOT NULL,
        FOREIGN KEY (id_pemesanan) REFERENCES Pemesanan (id_pemesanan),
        FOREIGN KEY (id_menu) REFERENCES Menu (id_menu))"""

cursor.execute(query)
print("Tabel DetailPemesanan Berhasil Dibuat")

cursor.execute("show tables")
print(cursor.fetchall())

print()

cursor.execute("DESC DetailPemesanan")
result = cursor.fetchall()
for row in result:
    print(row)