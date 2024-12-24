import mysql.connector

connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="",
    database="restaurant",
)

cursor = connection.cursor()
query = """CREATE TABLE IF NOT EXISTS Menu(
        id_menu INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_menu TEXT NOT NULL,
        kategori TEXT NOT NULL,
        harga REAL NOT NULL)
    """
cursor.execute(query)
print("Tabel Menu Berhasil Dibuat")

cursor.execute("show tables")
print(cursor.fetchall())

print()

cursor.execute("DESC Menu")
result = cursor.fetchall()
for row in result:
    print(row)