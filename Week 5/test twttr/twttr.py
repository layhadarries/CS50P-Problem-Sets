def main():
    text = input("Input: ")
    print(f'Ouput: {shorten(text)}')


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]

    for char in word:
        if char.lower() in vowels:
            new_txt = new_txt.replace(char, "")

    return new_txt


if __name__ == "__main__":
    main()
