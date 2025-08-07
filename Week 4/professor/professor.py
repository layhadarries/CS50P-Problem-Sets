"""
Order of operations:
1-  Get Level input
    check if positive int and either 1, 2 or 3.

2-  Get x and y value returned as random.randint
    returns a single randomly generated non-negative integer with level digits

    - 10 sums in total
    - 3 tries for each sum
    - score + 1 for correct answer ON FIRST TRY ONLY

3-  return score.

"""

import random


def get_level():
    levels = [1, 2, 3]

    while True:
        try:
            txt = int(input("Level: "))

            if txt in levels:
                return txt

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def generate_sum(x, y):
    answer = x + y
    tries = 0

    while tries < 3:
        try:
            txt = int(input(f'{x} + {y} = '))

            if txt == answer:
                return True
            else:
                tries += 1
                print("EEE")

        except ValueError:
            tries += 1
            print("EEE")

    print(f'{x} + {y} = {answer}')
    return False


def main():
    lvl = get_level()
    score = 0

    for sum in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)

        if generate_sum(x, y):
            score += 1

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
