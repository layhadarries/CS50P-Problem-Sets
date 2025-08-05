def main():
    convert = get_percentage()

    if convert >= 99 or convert == 100:
        print("F")
    elif convert <= 1 or convert == 0:
        print("E")
    else:
        print(f"{convert}%")


def get_percentage():
    while True:
        try:
            text = input("Fraction: ")
            x, y = map(int, text.split("/"))

            if y == 0 or y < 0 or x > y:
                continue

            return round(x / y * 100)  # round() handles floats

        # Error is raised if the input is NOT an int or anything else
        except (ValueError, ZeroDivisionError):
            pass  # test return


main()
