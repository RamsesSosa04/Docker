import mysql.connector

connection = mysql.connector.connect (
    host = "ls-ef4300d410ebc1a8304030b638b03ed2da87f5c1.c90u2ss6wl6d.us-east-2.rds.amazonaws.com",
    user = "dbmasteruser",
    password = "SicnoLab2025",
    database = "dbmastertest"
)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255))")
cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Roman')")
cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Jose')")
cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Thomas')")
connection.commit

cursor.execute("SELECT * FROM usuarios")
for file in cursor.fetchall():
    print(file)

cursor.close()
connection.close()