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
        text = input("Date: ").strip()

        if "/" in text:     # if input is "mm/dd/yyyy"
            try:
                mm, dd, yyyy = text.split("/")
                mm = int(mm)
                dd = int(dd)

                # Day and Month parameters, condition set to break the loop
                if (dd >= 1 and dd <= 31) and (mm >= 1 and mm <= 12):
                    break   # End the loop so that it only prints once!!

            except ValueError:
                # "when you want to ignore the error and retry (like prompting again for input)" not return, not continue.
                pass

        elif "," in text:  # If input is "month in months dd, yyyy"
            try:
                mm_text, dd, yyyy = text.replace(",", "").split(" ")
                dd = int(dd)

                if mm_text in months:
                    mm = months.index(mm_text, 1)

                    # Day parameters, condition set to break the loop
                    if dd >= 1 and dd <= 31:
                        break

            except ValueError:
                pass

    print(f'{yyyy}-{mm:02}-{dd:02}')


main()

# check50 cs50/problems/2022/python/outdated
# submit50 cs50/problems/2022/python/outdated
