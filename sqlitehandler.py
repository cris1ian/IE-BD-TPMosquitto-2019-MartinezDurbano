import json
import sqlite3

db_name = "iot-sqlite.db"


class DatabaseManager():
    def __init__(self):
        self.conn = sqlite3.connect(db_name)
        self.conn.commit()
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()

    def __del__(self):
        self.cur.close()
        self.conn.close()

	# Cristian: agregado método para consultas SQL
    def __get__(self, sql_query):
        self.cur.execute(sql_query)
        self.cur.execute(sql_query)
        self.conn.commit()
        return self.cur.fetchall()


def write_to_db(topic, jsonData):

    dbObj = DatabaseManager()
    data = json.loads(jsonData)
    table = str(topic)
	# Cristian: componer la sentencia SQL con el JSON que llega reemplazando caracteres no permitidos
    query = '''INSERT INTO '''+ table.replace("/","_") + '''(value, unit, timestamp) VALUES(?,?,?)'''
    print (query)
	# Cristian: escribo en la base de datos
    dbObj.add_del_update_db_record(query,( (data['value']), (data['unit']), (data['timestamp'])))
    del dbObj
#   actually write to the db now

# Cristian: agregada funcion para consultas SQL
def read_from_db(query):

    dbObj = DatabaseManager()
    result = dbObj.__get__(query)
    del dbObj
    return result
