def main():
    time = input("What time is it? ")

    flt = convert(time)
    if 7.0 <= flt <= 8.0:
        print("breakfast time")
    elif 12.0 <=flt <= 13.0:
        print("lunch time")
    elif 18.0 <=flt <= 19.0:
        print("dinner time")


def convert(time):
   hour , minutes = time.split(':')
   x = int(hour)
   y = int(minutes)
   v= x + (y/60)
   return v


if __name__ == "__main__":
    main()
