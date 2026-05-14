import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_finanzas"
)

cursor = conexion.cursor(dictionary=True)