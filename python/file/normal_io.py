def read_file(file_name):
    # read each line
    print("read each line")
    with open(file_name) as f:
        # data_list = f.readlines()
        # for data in data_list:
        for data in f:
            print(data)

    print("read at once")
    # read at once
    with open(file_name) as f:
        data = f.read()
        print(data)


def write_file(file_name):
    # write to file
    s = "hello writing!\n next line"
    # with open(file_name, mode="w") as f:
    #     f.write(s)

    # list, without new line
    l = ["first\n", "second", "third"]
    with open(file_name, mode="w") as f:
        f.writelines(l)

    # wit new line
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(l))


def add_to_file(file_name):
    s = "Add \n comment!"
    with open(file_name, mode="a") as f:
        f.write(s)


if __name__ == '__main__':
    input_file_name = "input.txt"
    read_file(input_file_name)
    save_file_name = "save_file.txt"
    write_file(save_file_name)
    add_to_file(save_file_name)
