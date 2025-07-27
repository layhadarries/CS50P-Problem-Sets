def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digit = False

    if len(s) < 7 and len(s) > 1:           # Plate must be less that 6, more than 2

        if s.isalnum():                     # Plate must contain onlu numbers and letters

            if s[:2].isdigit():             # Must start with 2 LETTERS, no digits
                return False

            else:

                for char in s:                  # Checking each character in string
                    if char.isdigit():          # If the character is a digit
                        # If character is not digit (digit is not true)
                        if not digit:
                            if char == '0':     # If the character is 0
                                return False    # False
                            digit = True        # if char.isdigit() and digit is not false then digit should equal true

                        else:
                            return True
        else:
            return False
    else:
        return False


main()

#   check50 cs50/problems/2022/python/plates
#   submit50 cs50/problems/2022/python/plates
