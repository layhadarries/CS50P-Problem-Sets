def main():
    text = input("camelCase : ")
    snake_case = ""             # Add adjusted text to an empty string

    for char in text:              # Check every character in text
        if char.isupper():         # Check if character is uppercase, returns true or false
            snake_case += "_" + char.lower() # add to empty string to create a new one with the _ placed before the found uppercase letter, turning it into lowercase
        else:
            snake_case += char     # If char is not upper, add to empty string and continue loop

    print("snake_case: ", snake_case)


main()
