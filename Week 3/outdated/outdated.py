ddef main():
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
                mm, dd, yyyy = map(int, date.split("/"))
                #   mm, dd, yyyy = text.split("/")     mm = int(mm)   dd = int(dd)

            elif "," in text:  # If input is "month in months dd, yyyy"
                mm_text, dd, yyyy = text.replace(",", "").split(" ")
                dd = int(dd)
                yyyy = int(yyyy)
                mm = months.index(mm_text, 0) + 1

            else:
                continue

            # Day and Month parameters, condition set to break the loop
            if (dd >= 1 and dd <= 31) and (mm >= 1 and mm <= 12):
                print(f'{yyyy}-{mm:02}-{dd:02}')
                break   # End the loop so that it only prints once!!

        except ValueError, IndexError:
            continue


main()

