import sys
import requests


def main():
    bitcoin = float(sys.argv[1])

    if len(sys.argv) != 2:  # cmd should be $python "bitoin.py"(argv 1) "2"(argv 2)
        sys.exit("Missing command-line argument")

    elif isinstance(bitcoin, float) is False:
        sys.exit("Command-line argument is not a number")

    try:
        api_key = "d12b469ce0c7d63263f7e00736de5afd43dcd4f332a18d749665fb8603ef7124"
        r = requests.get(
            f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}')
        data = r.json()
        priceUsd = float((data["data"]["priceUsd"]))

        amount = (priceUsd * bitcoin)

    except requests.RequestException:
        sys.exit("API request failed")

    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()

#   check50 cs50/problems/2022/python/bitcoin
#   submit50 cs50/problems/2022/python/bitcoin
