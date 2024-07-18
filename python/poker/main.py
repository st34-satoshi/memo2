import random
from collections import Counter

def wait_input():
    print('////////////')
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
    else:
        # 
        pass
    wait_input()

def random_select(i):
    cards = []
    for s in ['c', 'd', 'h', 's']:
        for n in range(13):
            cards.append(s + str(n+1))
    print(cards)
    return random.sample(cards, i)

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
    return v == [1, 1, 2]

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

def take_numbers(cards):
    numbers = []
    for c in cards:
        n = int(c[1:])
        numbers.append(n)
    return numbers


def is_flush(cards):
    s = cards[0][0]
    for c in cards:
        if s != c[0]:
            return False
    return True

    
if __name__ == '__main__':
    wait_input()