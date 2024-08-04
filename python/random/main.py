import random
import string

def random_number(d):
    return ''.join(random.choices(string.digits, k=d))


if __name__ == '__main__':
    for _ in range(10):
        print(f'F{random_number(8)}')