# see stock performance
# prepare for csv file for a year

import csv

class Transaction:

    def __init__(self, row):
        self.row = row
        self.date = row[0]
        self.symbol_name = row[1]
        self.symbol = row[2]
        self.is_cell = row[6] == "売却"
        self.type = row[7]
        self.num = int(row[8])
        self.price = row[9]

def read_csv(file_name):
    data = {}  # {symbol: [transition]}
    with open(file_name, "r", encoding="shift-jis") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 5 or '2021' not in row[0] :
                continue
            transition = Transaction(row)
            if transition.symbol in data:
                data[transition.symbol].append(transition)
            else:
                data[transition.symbol] = [transition]
    print(len(data))
    return data

def result(data):
    total = 0
    for transitions in data.values():
        for transition in transitions:
            if transition.is_cell and transition.symbol == 'NVDA' and transition.type == "一般預り":
                print(f'date = {transition.date}, num = {transition.num}')
                total += transition.num
    print(f'total = {total}')


if __name__ == '__main__':
    file = "sb.csv"
    data = read_csv(file)
    result(data)