def main():
    text = input("Input: ").replace('\n', '')
    vowels = ["a", "e", "i", "o", "u"]
    new_txt = ''

    for char in text:
        if char.lower() not in vowels:
            new_txt += char

    print(new_txt, end='')


main()
