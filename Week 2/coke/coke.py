def main():

    coins = {
        "25": 25,
        "10": 10,
        "5": 5
    }

    amount_due = 50

    while amount_due > 0:
        text = input("Insert coin: ")

        if text in coins:
            amount_due -= coins[text]

        if amount_due > 0:
            print(f'Amount due: {amount_due}')

        elif amount_due == 0:
            print('Change Owed: 0')

        else:
            print(f'Change Owed: {abs(amount_due)}')


main()
