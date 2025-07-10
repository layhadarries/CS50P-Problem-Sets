text = input()


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


print(convert(text))
