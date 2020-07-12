import sqlite3

def db_list(year):
    db = 'baseball_' + year +'.db'
    con = sqlite3.connect(db)
    cur = con.cursor()

    #dbから全員のデータ取得(sql文)
    cur.execute('SELECT games, ab, r, h, double, triple, hr, rbi, bb, so, sb, ba, slg, id, name FROM batter')

    #executeからリストに変換
    list_data =[]
    for data in cur:
        list_data.append({
            'games': data[0],
            'ab': data[1],
            'r': data[2],
            'h': data[3],
            '2h': data[4],
            '3h': data[5],
            'hr': data[6],
            'rbi': data[7],
            'bb': data[8],
            'so':data[9],
            'sb': data[10],
            'ba': data[11],
            'slg': data[12],
            'id': data[13],
            'name': data[14]
        })

    list = cur.fetchall()

    cur.close()
    con.close()

    return list_data

print(db_list('2019'))