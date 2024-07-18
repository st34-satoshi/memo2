import random
from collections import Counter, defaultdict
import itertools

def wait_input():
    print('////////////')
    print('q: 終了')
    print('r: ランダムに5枚取得する')
    print('カード5種類: 役を表示する')
    print('カードの入力方法: マーク(cdhs)数字(1~13), 例: "c1 d2 h3 s4 d1"')
    # club: ♣, diamond: ♦, hart: ♥, spade: ♠
    s = input()
    if s == "r":
        cards = random_select(5)
        print(f'取得したカード: {cards}')
        hand = hands(cards)
        print(f'役: {hand}')
    elif s == "q":
        return
    elif is_cards(s):
        cards = to_cards(s)
        hand = hands(cards)
        print(f'役: {hand}')
    else:
        print("入力が正しくありません")
    print()
    wait_input()

def to_cards(s):
    return s.split()

def is_cards(s):
    ss = s.split()
    if len(ss) != 5:
        return False
    for c in ss:
        if len(c) != 2 and len(c) != 3:
            return False
        if c[0] not in ['c', 'd', 'h', 's']:
            return False
        try:
            i = int(c[1:])
            if i < 1 and 13 < i:
                return False
        except:
            return False
    return True

def random_select(i):
    cards = all_cards()
    return random.sample(cards, i)

def all_cards():
    cards = []
    for s in ['c', 'd', 'h', 's']:
        for n in range(13):
            cards.append(s + str(n+1))
    return cards

def hands(cards):
    """
    役をstringで返す
    """
    if is_straight_flush(cards):
        numbers = take_numbers(cards)
        numbers.sort()
        if numbers == [1, 10, 11, 12, 13]:
            return "ロイヤルフラッシュ"
        return "ストレートフラッシュ"
    if is_four(cards):
        return "フォーカード"
    if is_full_house(cards):
        return "フルハウス"
    if is_flush(cards):
        return "フラッシュ"
    if is_straight(cards):
        return "ストレート"
    if is_three(cards):
        return "スリーカード"
    if is_two_pair(cards):
        return "ツーペア"
    if is_one_pair(cards):
        return "ワンペア"

    return "役なし"

def is_one_pair(cards):
    numbers = take_numbers(cards)
    counts = Counter(numbers)
    v = list(counts.values())
    v.sort()
    return v == [1, 1, 1, 2]

def is_two_pair(cards):
    numbers = take_numbers(cards)
    counts = Counter(numbers)
    v = list(counts.values())
    v.sort()
    return v == [1, 2, 2]

def is_three(cards):
    numbers = take_numbers(cards)
    counts = Counter(numbers)
    v = list(counts.values())
    v.sort()
    return v == [1, 1, 3]

def is_full_house(cards):
    numbers = take_numbers(cards)
    counts = Counter(numbers)
    return max(counts.values()) == 3 and min(counts.values()) == 2

def is_four(cards):
    numbers = take_numbers(cards)
    counts = Counter(numbers)
    v = max(counts.values())
    return v == 4

def is_straight_flush(cards):
    if not is_flush(cards):
        return False
    if not is_straight(cards):
        return False
    return True

def is_straight(cards):
    numbers = take_numbers(cards)
    numbers.sort()
    if numbers == [1, 10, 11, 12, 13]:
        return True
    for i in range(len(numbers) - 1):
        if numbers[i] + 1 != numbers[i+1]:
            return False
    return True

def is_flush(cards):
    s = cards[0][0]
    for c in cards:
        if s != c[0]:
            return False
    return True

def take_numbers(cards):
    numbers = []
    for c in cards:
        n = int(c[1:])
        numbers.append(n)
    return numbers


"""
全てのパターンを調べて役の計算が正しいか確認する
"""

def test_all():
    print("テスト開始")
    cards = all_cards()
    patterns = list(itertools.combinations(cards, 5))
    print(f'card pattern: {len(patterns) == 2598960}')

    hand_patterns = defaultdict(lambda: 0)
    for i, card_set in enumerate(patterns):
        if i % 100000 == 0:
            print(f"{i} / 2598960, {i*100//2598960}%")
        hand = hands(list(card_set))
        hand_patterns[hand] += 1
    
    # 参考サイト: https://mpj-portal.jp/forbeginners/hand-role-poker-hands-strength/
    print(hand_patterns)
    print(f'ロイヤルフラッシュ: {hand_patterns['ロイヤルフラッシュ'] == 4}')
    print(f'ストレートフラッシュ: {hand_patterns['ストレートフラッシュ'] == 36}')
    print(f'フォーカード: {hand_patterns['フォーカード'] == 624}')
    print(f'フルハウス: {hand_patterns['フルハウス'] == 3744}')
    print(f'フラッシュ: {hand_patterns['フラッシュ'] == 5108}')
    print(f'ストレート: {hand_patterns['ストレート'] == 10200}')
    print(f'スリーカード: {hand_patterns['スリーカード'] == 54912}')
    print(f'ツーペア: {hand_patterns['ツーペア'] == 123552}')
    print(f'ワンペア: {hand_patterns['ワンペア'] == 1098240}')


if __name__ == '__main__':
    wait_input()

    # テスト用
    # test_all()