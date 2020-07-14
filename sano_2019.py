#sano_list(取得したい年)
#入力した年の佐野選手の成績リストを返す

import sqlite3

def sano_list(year):
    conn = sqlite3.connect('baseball_' + year + '.db')
    cur = conn.cursor()

    cur.execute('SELECT games, ab, r, h, double, triple, hr, rbi, bb, so, sb, ba, slg, id, name FROM batter WHERE name="佐野 恵太"')

    for data in cur:
        list ={
            'games': data[0],
            'ab': data[1],
            'r': data[2],
            'h': data[3],
            '2h': data[4],
            '3h': data[5],
            'hr': data[6],
            'rbi': data[7],
            'bb': data[8],
            'so': data[9],
            'sb': data[10],
            'ba': data[11],
            'slg': data[12],
            'id': data[13],
            'name': data[14]
    }


    cur.close()
    conn.close()

    return list

sano_list('2019')