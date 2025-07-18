def main():
    question = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip())

    if question == "forty-two" or question == "forty two" or question == "42":
        answer("yes")
    else:
        answer("no")

def answer(n):
    print(n)

main()
