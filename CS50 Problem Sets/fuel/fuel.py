def main():
    while True: # Loop indefinitely until valid input is received and processed
        try:
            fraction = input("Fraction: ")
            x_str, y_str = fraction.split("/")

            x = int(x_str)
            y = int(y_str)

            # Rule 1: Y cannot be 0
            if y == 0:
                # print("Error: Denominator cannot be zero. Please try again.") # Optional: for user feedback
                continue # Go back to the start of the while loop to reprompt

            # Rule 2: X cannot be greater than Y
            if x > y:
                # print("Error: Numerator cannot be greater than denominator. Please try again.") # Optional: for user feedback
                continue # Go back to the start of the while loop to reprompt

            # Calculate percentage
            percentage = (x / y) * 100

            # Rule 3: Output E, F, or percentage
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")

            # If we reach here, all input was valid and output was printed, so break the loop
            break

        except ValueError:
            # This catches errors from:
            # 1. fraction.split("/") if input doesn't contain a single "/" (e.g., "5-10", "1/2/3")
            # 2. int(x_str) or int(y_str) if X or Y are not valid integers (e.g., "three", "1.5")
            # print("Error: Invalid input. Please enter a fraction like X/Y where X and Y are integers. Try again.") # Optional: for user feedback
            continue # Go back to the start of the while loop to reprompt

        except ZeroDivisionError:
            # Although we have an explicit check for y == 0, it's good practice to catch ZeroDivisionError
            # here too, just in case (e.g., if the explicit check was missed or for robustness).
            # print("Error: Cannot divide by zero. Please try again.") # Optional: for user feedback
            continue # Go back to the start of the while loop to reprompt


# Standard boilerplate to call main() when the script is executed
if __name__ == "__main__":
    main()
