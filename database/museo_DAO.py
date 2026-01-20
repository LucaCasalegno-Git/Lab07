import mysql

from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_musei() -> list[Museo] | None:

        cnx = ConnessioneDB.get_connection()
        result = []

        if cnx is None:
            print("Errore connessione db")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM museo"

        try:
            cursor.execute(query)
            for row in cursor:
                museo = Museo(id=row['id'], nome=row['nome'], tipologia=row['tipologia'])
                result.append(museo)
        except Exception as e:
            print(f"Errore get musei: {e}")
        finally:
            cursor.close()
            cnx.close()

        return result










