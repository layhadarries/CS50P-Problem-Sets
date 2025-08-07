#   WITHOUT inflect
"""
def main():
    name_list = []

    while True:
        try:
            text = input("Name: ")
            name_list.append(text)

        except EOFError:

            if len(name_list) == 1:
                print(f'Adieu, adieu, to {name_list[0]}')

            elif len(name_list) == 2:
                print(f'Adieu, adieu, to {"and".join(name_list)}')

            elif len(name_list) > 2:
                print(
                    f'Adieu, adieu, to {", ".join(name_list[0:-1])} and {name_list[-1]}')
                #                       all names up until the last       the last name

            print("\n")
            break


main()
"""

import inflect


def main():
    p = inflect.engine()
    name_list = []

    while True:
        try:
            text = input("Name: ")
            name_list.append(text)

        except EOFError:
            print(f'Adieu, adieu, to {p.join(name_list)}')
            print("\n")
            break


if __name__ == "__main__":
    main()

#   check50 cs50/problems/2022/python/adieu
#   submit50 cs50/problems/2022/python/adieu
