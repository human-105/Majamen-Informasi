import mysql.connector

connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="",
    database="",
)


cursor = connection.cursor()
if connection :
    print("Berhasil Terhubung ke DataBase")

cursor.execute('CREATE DATABASE restaurant')
print('Database Berhasil Dibuat')

cursor.execute("show databases")
print(cursor.fetchall())

result = cursor.fetchall()
for item in result:
    print(item)