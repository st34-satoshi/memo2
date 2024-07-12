import chess.pgn
from collections import defaultdict
import os
import chess.svg
import cairosvg
from stockfish import Stockfish
stockfish = Stockfish(depth=15)

def is_search(game):
    MIN_R = 2000
    black_elo = int(game.headers["BlackElo"])
    white_elo = int(game.headers["WhiteElo"])
    if black_elo < MIN_R or white_elo < MIN_R:
        return False
    return True

def save_image(board, white, black, n, move):
    board_svg = chess.svg.board(board)
    f = open("position.svg", "w")
    f.write(board_svg)
    f.close()
    img = cairosvg.svg2png(url='position.svg', write_to=f'blunders/{white}-{black}-{n}-{move}.png', scale=7)

def compute_white_value(fen):
    stockfish.set_fen_position(fen)
    evaluation = stockfish.get_evaluation()
    next_value = None
    if evaluation['type'] == 'cp':
        next_value = evaluation['value'] / 100.0
    else:
        if evaluation['value'] > 0:
            next_value = 99 # mate
        else:
            next_value = -99
    return next_value


if __name__ == '__main__':
    directory = 'data'
    files = os.listdir(directory)
    game_cnt = 0
    blunder_cnt = 0
    rounds = defaultdict(lambda: 0)
    for file in files:
        if ".pgn" not in file:
            continue
        pgn = open(f"{directory}/{file}")
        for _ in range(300):
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            ok = is_search(game)
            if(not ok):
                break
            board = game.board()
            previous_value = 0
            print('game start')
            values = []
            for i, move in enumerate(game.mainline_moves()):
                previous_fen = board.fen()
                board.push(move)
                next_value = compute_white_value(board.fen())
                values.append(next_value)
                # check diff
                if abs(previous_value - next_value) > 2 and (abs(previous_value) < 5 or abs(next_value) < 5):
                    # プレーヤーが指したことで評価値が変わった
                    blunder_cnt += 1
                    save_image(board, game.headers["White"], game.headers["Black"], i, move)
                    print(f'blunder, {game.headers["White"]} vs {game.headers["Black"]}, moves = {i // 2}, next move = {move}')
                    print(previous_fen)
                previous_value = next_value
            print(values)
            game_cnt += 1
            rounds[game.headers["Round"]] += 1
    print(f'total game = {game_cnt}')
    print(f'total blunder = {blunder_cnt}')
    print(rounds)