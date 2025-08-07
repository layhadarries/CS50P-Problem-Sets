import random


def lvl_input(text):
    while True:
        try:
            lvl_int = int(input(text))

            if lvl_int > 0:  # must be a positive integer
                return lvl_int

        except ValueError:  # check if input is only an int
            pass


def main():
    level = lvl_input("Level: ")
    rand_int = random.randint(1, level)     # random n between 1 and level

    while True:
        try:
            guess_int = int(input("Guess: "))

        except ValueError:  # check if input is only an int
            continue

        if guess_int <= 0:
            continue

        if guess_int < rand_int:    # if smaller than guess
            print("Too small!")

        elif guess_int > rand_int:  # if bigger than guess
            print("Too large!")

        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
