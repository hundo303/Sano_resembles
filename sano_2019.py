import sqlite3

def sano_2019():
    conn = sqlite3.connect('baseball_2019.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM batter WHERE name="佐野 恵太"')

    list = cur.fetchone()

    print(list)

    cur.close()
    conn.close()
