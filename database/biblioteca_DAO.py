from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def index(self):
        conn = DBConnect.get_connection()
        if conn is not None:
            print("Connection established")
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM biblioteca"
            cursor.execute(query)
            biblioteche = []
            for row in cursor:
                b = Biblioteca(row["id"], row["nome"], row["indirizzo"])
                biblioteche.append(b)

            cursor.close()
            conn.close()
            return biblioteche