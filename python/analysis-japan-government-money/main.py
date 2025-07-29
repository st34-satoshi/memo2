import csv
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def load_expenditure_data():
    """支出先データを読み込む関数"""
    data_path = Path("data/5-3_RS_2024_支出先_費目・使途.csv")
    
    data = []
    with open(data_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
            
    return data

def count_occurrences(data, header):
    """指定したヘッダーの値の出現回数をカウントする関数"""
    counter = Counter()
    total = 0
    for row in data:
        value = row[header]
        if value:
            counter[value] += 1
            total += 1
    print(counter)
    print(f"合計: {total}")

def sum_values(data, header):
    """指定したヘッダーの値の合計を計算する関数"""
    total = 0
    for row in data:
        # s = row['府省庁']
        # if s != '厚生労働省':
        #     continue
        value = row[header]
        if value:
            total += float(value)
    print(f"合計: {'{:,.0f}'.format(total)}")

def count_each_destination_money(data):
    """各支出先の金額をカウントする関数"""
    counter = Counter()
    total = 0
    for row in data:
        name = row['支出先名']
        price = row['金額']
        if price:
            total += float(price)
        if name and price:
            counter[name] += float(price)

    # 金額の大きい順にソートして上位10件を出力
    for name, amount in counter.most_common(10):
        print(f"{name}: ¥{'{:,.0f}'.format(amount)}")

    # 円グラフを作成
    # トップ10の金額を合計
    top10_total = sum(amount for _, amount in counter.most_common(10))
    # グラフ用のデータ準備
    labels = []
    sizes = []
    # トップ10のデータを追加
    for name, amount in counter.most_common(10):
        labels.append(name)
        sizes.append(amount)
    # その他を追加
    others = total - top10_total
    labels.append("その他")
    sizes.append(others)
    # グラフ描画（時計回りで大きいものから表示）
    plt.figure(figsize=(12, 8))
    # 色のリストを作成（その他を最後に異なる色にする）
    colors = list(plt.cm.Set3(np.linspace(0, 1, len(labels))))
    # その他の色を明るいグレーに変更
    colors[-1] = '#CCCCCC'
    
    # 割合と金額を表示する関数
    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = pct*total/100.0 / 1000000000000
            return f'{pct:.1f}% ({val:.1f}兆円)'
        return my_autopct
    
    plt.pie(sizes, labels=labels, autopct=make_autopct(sizes), startangle=90, counterclock=False, colors=colors)
    plt.axis('equal')
    plt.title('支出先別金額: 合計96,259,695,151,177円')
    # plt.show()
    plt.savefig('output/支出先別金額.png')


def main():
    print("Hello")
    data = load_expenditure_data()
    print(len(data))
    count_occurrences(data, '府省庁')
    sum_values(data, '金額')
    count_each_destination_money(data)


if __name__ == "__main__":
    main()
