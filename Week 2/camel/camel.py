def main():
    text = input("camelCase : ")
    snake_case = ""             # Add adjusted text to an empty string

    for c in text:              # Check every character in text
        if c.isupper():         # Check if character is uppercase, returns true or false
            # add to empty string to create a new one with the _ placed before the found uppercase letter, turning it into lowercase
            snake_case += "_" + c.lower()
        else:
            snake_case += c     # If char is not upper, add to empty string and continue loop

    print("snake_case: ", snake_case)


main()
