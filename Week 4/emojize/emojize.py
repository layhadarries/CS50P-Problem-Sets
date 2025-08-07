import emoji


def main():
    text = input("")
    # Check pip emoji API on how to print different emoji types
    print(emoji.emojize(f"Output: {text}", language='alias'))


if __name__ == "__main__":
    main()
