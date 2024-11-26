"""
ラウンドロビンでペアリングをする方法
適当にペアリングしてもなんとかなる
"""

def generate_round_robin_pairings(players):
    """
    8人のプレーヤーのラウンドロビン対戦表を生成する
    
    Args:
        players (list): 8人のプレーヤー名のリスト
    
    Returns:
        list: 各ラウンドの対戦カードのリスト
    """
    if len(players) != 8:
        raise ValueError("プレーヤーは8人である必要があります")
        
    # 7ラウンド必要
    rounds = []
    for round_num in range(7):
        # 各ラウンドで4試合
        round_pairings = []
        # プレーヤーをローテーションさせる
        # 1人目は固定して、残りを時計回りにシフト
        rotated_players = players[1:]
        shift = round_num
        rotated_players = (rotated_players[-shift:] + 
                         rotated_players[:-shift])
        
        # ペアを作成
        for i in range(4):
            if i == 0:
                # 1人目は固定プレーヤーとペア
                pair = (players[0], rotated_players[0])
            else:
                # 残りのプレーヤーで順にペア
                pair = (rotated_players[i], 
                       rotated_players[-(i)])
            round_pairings.append(pair)
            
        rounds.append(round_pairings)
    
    return rounds

def print_tournament_schedule(rounds):
    """
    対戦表を見やすく出力する
    
    Args:
        rounds (list): generate_round_robin_pairings()の戻り値
    """
    for round_num, round_pairs in enumerate(rounds, 1):
        print(f"\nラウンド {round_num}:")
        for pair in round_pairs:
            print(f"{pair[0]} vs {pair[1]}")


def decide_paring_at(parings, round_num):
    """
    ラウンドのペアリングを決める
    paringsに含まれている人とはペアにならない
    そのラウンドでペアが決められなければエラー
    ペアリングの数を返す
    """
    ok = True
    for p in parings.values():
        if len(p) != round_num:
            ok = False
            break
    if ok:
        # 次のラウンドのペアリングを決める
        if round_num == 7:
            return 1
        return decide_paring_at(parings, round_num + 1)
    
    count = 0
    # 現在のラウンドのペアが決めっていない人がいる
    for i in range(len(parings.keys())):
        if len(parings[i]) == round_num:
            # すでにこのラウンドでペアリングが決まっている
            continue
        # ペアリングが決まっていない。残りのペアが決まっていない人の中から1人選ぶ
        alone = True
        for j in range(len(parings)):
            if i == j:
                continue
            if j not in parings[i] and len(parings[j]) < round_num:
                parings[i].append(j)
                parings[j].append(i)
                alone = False
                count += decide_paring_at(parings, round_num)
                parings[i].remove(j)
                parings[j].remove(i)
        if alone:
            print('ERROR: No Paring')
            print(i)
            print(parings)
            print(round_num)
    return count



if __name__ == "__main__":
    # 8人のプレーヤーのラウンドロビンの組み合わせを出力する
    players = ["Player1", "Player2", "Player3", "Player4",
              "Player5", "Player6", "Player7", "Player8"]
    rounds = generate_round_robin_pairings(players)
    print_tournament_schedule(rounds)

    # 8人のプレーヤーの組み合わせの場合の数を求める
    # 適当にペアリングをすると同じ人と対局することになる人が出る
    # 終わらない...
    # pairings = {0: [1], 1: [0], 2: [3], 3: [2], 4: [5], 5: [4], 6: [7], 7: [6]} # 最初のペアリングは決める
    # count = decide_paring_at(pairings, 1)
    # print(count)