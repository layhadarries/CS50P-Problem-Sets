def main():
    text = input("Input: ")
    vowels = ["a", "e", "i", "o", "u"]
    new_txt = ''

    for char in text:
        if char not in vowels:
            new_txt += char
        else:
            continue

    print(new_txt)


main()
