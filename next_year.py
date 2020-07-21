import sqlite3


def next_year(player_name, previous_year):
    db = 'baseball_' + str(previous_year + 1) + '.db'
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(f'SELECT games, ab, r, h, double, triple, hr, rbi, bb, so, sb, ba, slg, id, name FROM batter WHERE name="{player_name}"')

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

    return list

print(next_year('佐野 恵太', 2018))
