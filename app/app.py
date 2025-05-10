import mysql.connector

connection = mysql.connector.connect (
    host = "",
    user = "",
    password = "SicnoLab2025",
    database = "dbmastertest"
)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255))")
cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Roman')")
connection.commit

cursor.execute("SELECT * FROM usuarios")
for file in cursor.fetchall():
    print(file)

cursor.close()
connection.close()
