def main():

    text = input("Input: ")
    vowels = ["a", "e", "i", "o", "u"]

    for char in text:
        if char.lower() in vowels:
            text = text.replace(char, "")
    print(f"Output: {x}")


main()
