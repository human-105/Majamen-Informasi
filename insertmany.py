import mysql.connector

connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="",
    database="restaurant",
)

cursor = connection.cursor()
nama_menu = input("Masukkan nama menu: ")
kategori = input("Masukkan kategori : ")
harga = input("Masukkan harga : ")

insert_query = "INSERT INTO Menu (nama_menu, kategori, harga) VALUES (%s,%s,%s)"
cursor.execute(insert_query, (nama_menu, kategori, harga))

connection.commit()
print(f"Data Menu '{nama_menu}' berhasil ditambahakan!")
cursor.close()
connection.close()