def main():
    greeting = str(input("Greeting: ").lower().strip(' '))
    print(greeting)

    if greeting.startswith('hello'):
        cash("$0")
    elif greeting.startswith('h'):
        cash("$20")
    else:
        cash("$100")

def cash(n):
    print(n)

main()
