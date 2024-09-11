def read_file(filename):
    counter = {"M": 0, "F": 0, "X": 0}
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                if i % 10000 == 0:
                    print(i)
                sex = line[80]
                if sex == "M":
                    counter["M"] += 1
                elif sex == "F":
                    counter["F"] += 1
                else:
                    counter["X"] += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Unable to read file '{filename}'.")
    print(counter)
    print(f'female rate = {counter["F"] / (counter["F"] + counter["M"]) * 100}%')
    print(f'men rate = {counter["M"] / (counter["F"] + counter["M"]) * 100}%')


if __name__ == "__main__":
    read_file("players_list_foa.txt")