def main():
    text = input("Plate: ")

    if is_valid(text):
        print("Valid")
    else:
        print("Invalid")


def is_valid(text):
    digit = False

    if len(text) < 2 or len(text) > 6:
        return False

    if not text[0:2].isalpha():
        return False

    if not text.isalnum():
        return False

    for char in text:
        if char.isdigit():
            if not digit:
                if char == '0':
                    return False
                digit = True

        elif start:
            return False

    return True


main()
