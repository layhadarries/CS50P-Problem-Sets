def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            text = input("Date: ").strip()
    
            if "/" in text:     # if input is "mm/dd/yyyy"
                try:
                    mm, dd, yyyy = map(int, date.split("/"))
                #   mm, dd, yyyy = text.split("/")     mm = int(mm)   dd = int(dd)

                    # Day and Month parameters, condition set to break the loop
                    if (dd >= 1 and dd <= 31) and (mm >= 1 and mm <= 12):
                        break   # End the loop so that it only prints once!!

                except ValueError:
                    continue

            elif "," in text:  # If input is "month in months dd, yyyy"
                try:
                    mm_text, dd, yyyy = text.replace(",", "").split(" ")
                    dd = int(dd)
                    mm = months.index(mm_text, 0) + 1

                    # Day parameters, condition set to break the loop
                    if dd >= 1 and dd <= 31:
                        break

                except ValueError, IndexError:
                    continue

    print(f'{yyyy}-{mm:02}-{dd:02}')


main()
