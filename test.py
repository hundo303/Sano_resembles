import sqlite3

def db_list(year):
    db = 'baseball_' + year +'.db'
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute('SELECT ba, slg, name FROM batter')

    list_test = []
    for a in cur:
        list_test.append({
            'ba': a[0],
            'slg': a[1],
        })

    print(list_test[0])

    cur.close()
    con.close()


db_list('2019')