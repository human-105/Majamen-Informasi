import mysql.connector

connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="",
    database="restaurant",
)

cursor = connection.cursor()
query = """CREATE TABLE IF NOT EXISTS Pelanggan( 
        id_pelanggan INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        nomor_telepon TEXT NOT NULL)
    """
cursor.execute(query)
print("Tabel Pelanggan Berhasil Dibuat")

cursor.execute("show tables")
print(cursor.fetchall())

print()

cursor.execute("DESC Pelanggan")
result = cursor.fetchall()
for row in result:
    print(row)