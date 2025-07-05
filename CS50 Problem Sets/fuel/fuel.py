def main():
    while True: 
        try:
            fraction = input("Fraction: ")
            x_str, y_str = fraction.split("/")

            x = int(x_str)
            y = int(y_str)

            if y == 0:
                continue # Go back to the start of the while loop to reprompt

            if x > y:
                continue # Go back to the start of the while loop to reprompt
            percentage = (x / y) * 100

           
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")

            break

        except ValueError:
            continue # Go back to the start of the while loop to reprompt

        except ZeroDivisionError:
            continue # Go back to the start of the while loop to reprompt

if __name__ == "__main__":
    main()
