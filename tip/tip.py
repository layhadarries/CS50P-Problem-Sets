def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    a = d.strip("$")
    float_a = float(a) / 100
    return float_a


def percent_to_float(p):
    b = p.strip("%")
    float_b = float(b)
    return float_b


main()
