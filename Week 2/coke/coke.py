def main():
    coins = {
    "25": 25,
    "10": 10,
    "5": 5
}

    amount_due = 50

    while amount_due > 0:                       #   This function runs until amount due is 0
        text = input("Insert Coin: ")
        if text in coins:                       #   If the value inserted is in the coins dictionary
            amount_due -= coins[text]           #   amount due = 50 - the coin found in text
        else:
            print(f"Amount Due: {amount_due}")  #   If you input is not found in coins, print the amount due

        if amount_due > 0:                      #
            print(f"Amount Due: {amount_due}")

        elif amount_due == 0:
            print("Change Owed: 0")

        else:
            print(f"Change Owed: {-amount_due}")

main()
