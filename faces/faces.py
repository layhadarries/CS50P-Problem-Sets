text = input()


def convert(text):
    replace_emoji = text.replace(":)", "🙂").replace(":(", "🙁")
    return replace_emoji


print(convert(text))
