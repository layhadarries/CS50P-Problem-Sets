def main():
    while True:
        try:
            a = convert(input("Fraction: "))
            b = gauge(a)

            print(b)

        except ValueError:
            pass


def convert(fraction):
    while True:
        try:
            num, denom = fraction.split("/")
            x = int(num)
            y = int(denom)

            if y == 0:
                raise ZeroDivisionError()
            if y < 0:
                raise ValueError()
            if x > y:
                raise ValueError()

            return round(x / y * 100)

        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):

    if percentage >= 99 or percentage == 100:
        return "F"
    elif percentage <= 1 or percentage == 0:
        return "E"
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
