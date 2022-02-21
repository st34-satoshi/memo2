import csv


def write_csv(file_name):
    one_list = ["one", "two", "three", 4, 5, 6]
    two_list = [["one", "two"], [1, 2], [True, False]]
    with open(file_name, "w") as f:
        writer = csv.writer(f, lineterminator='\n')  # set new line code
        writer.writerow(one_list)
        writer.writerows(two_list)


def read_csv(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header
        for row in reader:
            print(row)


if __name__ == '__main__':
    save_file_name = "save_file.csv"
    write_csv(save_file_name)
    read_csv(save_file_name)