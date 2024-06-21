import chess.pgn
from collections import defaultdict
import os

if __name__ == '__main__':
    directory = 'data'
    files = os.listdir(directory)
    print(files)
    cnt = 0
    rounds = defaultdict(lambda: 0)
    for file in files:
        if ".pgn" not in file:
            continue
        pgn = open(f"{directory}/{file}")
        for _ in range(300):
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            cnt += 1
            rounds[game.headers["Round"]] += 1
            # print(game.headers["Round"])
    print(f'total game = {cnt}')
    print(rounds)