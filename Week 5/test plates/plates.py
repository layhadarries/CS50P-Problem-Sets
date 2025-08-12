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


if __name__ == "__main__":
    main()


"""
def is_valid(plate):
    # Checks if alphanumeric
    if plate.isalnum():
        #Checks if length is allowed
        if 2 <= len(plate) <= 6:
            #Checks if first 2 characters are letters
            if plate[0].isalpha() and plate[1].isalpha():
                #Finds number finder as a boolean and then
                number_finder = False
                for char in plate:
                    if char.isdigit():
                        number_finder = True
                    #If the boolean is true and a letter is found afterwards
                    elif number_finder and char.isalpha():
                        return False
                #Checks to see if first digit is 0
                for char in plate:
                    if char.isdigit():
                        if char == '0':
                            return False
                        break        
                return True 
            else:
                return False
        else:
            return False     
    else:
        return False

"""
