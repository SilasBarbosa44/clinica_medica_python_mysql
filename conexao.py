import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="clinica_medica",
            port=3306
        )
        
        if conn.is_connected():
            print("Banco de dados conectado com sucesso !")
            return conn
        
    except Error as e:
        print(f"Erro ao conectar no banco de dados {e}")
        return None