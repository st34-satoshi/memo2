import csv
from pathlib import Path
from collections import Counter

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


def main():
    print("Hello from analysis-japan-government-money!")
    data = load_expenditure_data()
    print(len(data))
    count_occurrences(data, '府省庁')


if __name__ == "__main__":
    main()
