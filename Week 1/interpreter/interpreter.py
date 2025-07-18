def main():
    text = input("Expression: ").split(' ')
    mylist = text

    x = float(mylist[0])
    expression = mylist[1]
    y = float(mylist[2])


    if expression == "+":
       equation(x + y)
    elif expression == "-":
       equation(x - y)
    elif expression == "*":
       equation(x * y)
    elif expression == "/":
       equation(x / y)
    else:
        return

def equation(n):
    print(float(n))

main()
