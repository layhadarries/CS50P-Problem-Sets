def main():
    dict = {}    # add every input to an epmty dictionary

    while True:         # Loop
        try:
            item = input("").strip().upper()    # Return item in caps

            if item:    # Creating a list since we have none
                if item in dict:
                    # Keep adding 1 to every reoccuring item
                    dict[item] += 1
                else:
                    dict[item] = 1       # Item added to list equals 1

        except EOFError:    # Control Z
            print("\n")

            # sort Keys in dictionary alphabetically
            for item in sorted(dict):
                print(f"{item}: {dict[item]}")

            break


main()

#    https://greenteapress.com/thinkpython2/html/thinkpython2012.html#sec131
#    check50 cs50/problems/2022/python/grocery
#   submit50 cs50/problems/2022/python/grocery
