import pandas as pd
import sqlite3

def db_list(year):
    db = 'baseball' + year +'.db'
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute('SELECT * FROM batter')

    list = cur.fetchall()

    cur.close()
    con.close()

    return list

def