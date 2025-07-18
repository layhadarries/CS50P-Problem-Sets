def main():
    time = input("What time is it? ")
    convert_time = convert(time)

    if convert_time >= 7 and convert_time <= 8:
        print("breakfast time")
    elif convert_time >= 12 and convert_time <= 13:
        print("lunch time")
    elif convert_time >= 18 and convert_time <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    hour, minute = time.split(":")
    return float(hour) + (float(minute) / 60)


if __name__ == "__main__":
    main()
