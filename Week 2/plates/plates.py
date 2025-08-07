def main():
    plate = input("Plate: ").strip().upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digit = False

    if len(s) < 7 and len(s) > 1:

        if s.isalnum():

            if s[:2].isdigit() or not s[-1].isalpha() and not s[-1].isdigit():
                return False

            else:

                for i in range(len(s)):
                    if s[i].isdigit():

                        if not digit:
                            if s[i] == '0':
                                return False
                            digit = True

                    elif digit:
                        return False

                return True

        else:
            return False

    else:
        return False


main()
