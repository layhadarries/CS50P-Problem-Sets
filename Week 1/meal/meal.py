#    Take time string '7:30'
#    Convert into float while calculating for time(minutes) ('7:30' = '7.5')
#    Print the meal time if it's within the time range, Return nothing if not

def main():
    time = input("What time is it? ")
    convert_time = convert(time)                       #    Gets the 'converted time' from the input to get Meal Times

    if convert_time >= 7 and convert_time <= 8:        #    Breakfast is within 7 and 8am
        print("breakfast time")
    elif convert_time >= 12 and convert_time <= 13:    #    Lunch is within 12 and 13pm
        print("lunch time")
    elif convert_time >= 18 and convert_time <= 19:    #    Dinner is within 18 and 19pm
        print("dinner time")
    else:
        return

 
def convert(time):
    hour, minute = time.split(":")
    return float(hour) + (float(minute) / 60)

#    https://www.youtube.com/watch?v=3dHyS1W4TIE <- Explains the following:
if __name__ == "__main__":
    main()
