import emoji


def main():
    text = input("")
    # Check pip emoji API on how to print different emoji types
    print(emoji.emojize(f"Output: {text}", language='alias'))


main()

#   check50 cs50/problems/2022/python/emojize
#   submit50 cs50/problems/2022/python/emojize
