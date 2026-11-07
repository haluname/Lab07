from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def index_generi(self):
        conn = DBConnect.get_connection()
        if conn is not None:
            print("Connection established")
            cursor = conn.cursor(dictionary=True)
            query = "SELECT DISTINCT genere FROM libro"
            cursor.execute(query)
            generi = []
            for row in cursor:
                g = row["genere"]
                generi.append(g)

            cursor.close()
            conn.close()
            return generi

    def filter(self, b, g):
        conn = DBConnect.get_connection()
        if conn is not None:
            print("Connection established")
            cursor = conn.cursor()
            query = "SELECT * FROM libro"
            condizioni = []
            valori = []
            if b != "Nessun Filtro":
                condizioni.append("id_biblioteca = %s")
                valori.append(b)

            if g != "Nessun Filtro":
                condizioni.append("genere = %s")
                valori.append(g)
            if condizioni:
                query += " WHERE " + " AND ".join(condizioni)

            cursor.execute(query, tuple(valori))

            libri = []
            for row in cursor:
                libri.append(Libro(row[0], row[1], row[2], row[3], row[4], row[5]))

            cursor.close()
            conn.close()
            return libri

