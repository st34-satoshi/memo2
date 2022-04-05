# see stock performance
# prepare for csv file for a year

import csv

class Transaction:

    def __init__(self, row):
        self.row = row
        self.date = row[1]
        self.symbol = row[2]
        self.symbol_name = row[3]
        self.type = row[4]
        self.is_cell = row[7] == "売"
        self.price = int(row[12])
        self.commission = int(row[13])

    def get_price(self):
        if self.is_cell:
            return self.price
        else:
            return self.price * -1


def read_csv(file_name):
    data = {}  # {symbol: [transition]}
    with open(file_name, "r", encoding="shift-jis") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 10 or row[4] not in ['特定', 'NISA'] or '2022' in row[0] :
                continue
            transition = Transaction(row)
            if transition.symbol in data:
                data[transition.symbol].append(transition)
            else:
                data[transition.symbol] = [transition]
    print(len(data))
    return data

def print_each_symbol_result(data):
    total = 0
    for transitions in data.values():
        if len(transitions) % 2 == 1:
            print(transitions[0].symbol_name)
            for transition in transitions:
                print(transition.get_price())
            continue
        diff = 0
        for transition in transitions:
            diff += transition.get_price()
        total += diff
    print(f'total = {total}')


if __name__ == '__main__':
    file = "mti.csv"
    data = read_csv(file)
    print_each_symbol_result(data)