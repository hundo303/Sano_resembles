import pandas as pd
import sqlite3

#dbの取得
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

    cur.close()
    con.close()

    return list_data

#比較してポイントのリストを返す
def comparison(main_list, year):
    point_list = {
        'game': 20,
        'ab':  75,
        'r': 10,
        'h': 15,
        '2h': 5,
        '3h': 4,
        'hr': 2,
        'rbi': 10,
        'bb': 25,
        'so': 150,
        'sb': 20,
        'ba': 0.001,
        'slg': 0.002
    }

    all_list = db_list(year)

    #ポイントのついたリストの生成
    player_point_list = []
    for player_score_list in all_list:
        player_point_list.append([player_score_list['id'], player_score_list['name']])
        for player, player_main, point in zip(player_score_list, main_list, point_list):
            abs(player - player_main) / point

def ask_score(player_score_list, main_list):
    point_list = {
        'game': 20,
        'ab':  75,
        'r': 10,
        'h': 15,
        '2h': 5,
        '3h': 4,
        'hr': 2,
        'rbi': 10,
        'bb': 25,
        'so': 150,
        'sb': 20,
        'ba': 0.001,
        'slg': 0.002
    }

    point_result = 1000
    for player_score, player_score_main, point in zip(player_score_list, main_list, point_list):
        point_result -= abs(player_score - player_score_main) / point
