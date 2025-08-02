def main():
    convert = get_percentage()

    if convert >= 99 or convert == 100:
        print("F")
    elif convert <= 1 or convert == 0:
        print("E")
    else:
        print(f"{convert}%")


def get_percentage():

    #   We want to keep prompting the user for an input.
    while True:
        try:
            text = input("Fraction: ")
            num, denom = text.split("/")

            # Converts string into int. Need it to check if the input is not an int
            x = int(num)
            y = int(denom)

            if y == 0:
                raise ZeroDivisionError()
            if y < 0:
                raise ValueError()
            if x > y:
                raise ValueError()

            return round(x / y * 100)  # round() handles floats

        # Error is raised if the input is NOT an int
        except (ValueError, ZeroDivisionError):
            pass  # test return


main()

# check50 cs50/problems/2022/python/fuel
# submit50 cs50/problems/2022/python/fuel
