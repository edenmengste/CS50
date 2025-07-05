import random

def main():
    level = get_level()
    score = 0

    for _ in range(10): # Loop for 10 problems
        # Fix 1: Call generate_integer twice to get X and Y
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y # Store the correct answer

        tries = 0
        while tries < 3: # Loop for up to 3 tries per problem
            # Fix 2B: Print the problem first, then get input without a prompt
            print(f"{x} + {y} = ", end="") # Use end="" to keep the cursor on the same line
            try:
                user_answer_str = input() # Get input from the user (no prompt here)
                user_answer = int(user_answer_str) # Convert user's input to integer

                if user_answer == correct_answer:
                    score += 1 # Correct answer
                    break      # Exit the 'tries' loop, move to next problem
                else:
                    print("EEE") # Incorrect answer
                    tries += 1   # Increment try count
            except ValueError:
                # User's input was not an integer
                print("EEE")
                tries += 1       # Increment try count

        # If 3 tries are exhausted (or user kept entering invalid input)
        if tries == 3:
            print(f"{x} + {y} = {correct_answer}") # Show the correct answer

    print(f"Score: {score}") # Final score output


def get_level():
    # Fix 3: Use a while True loop for re-prompting
    while True:
        try:
            # Fix 2A: Remove the prompt string "Level: "
            level_str = input()
            level_int = int(level_str) # Convert input to integer

            if level_int in [1, 2, 3]: # Check if level is 1, 2, or 3
                return level_int # Return valid level and exit function
            else:
                # If valid integer but not 1, 2, or 3, loop again
                pass # The loop will continue
        except ValueError:
            # If input is not a valid integer, loop again
            pass # The loop will continue


def generate_integer(level):
    # Fix 1 & 1b: Generate and return only ONE integer, and include 0 for level 1
    if level == 1:
        return random.randint(0, 9) # 0-9 (non-negative, 1-digit)
    elif level == 2:
        return random.randint(10, 99) # 10-99 (2-digit)
    elif level == 3:
        return random.randint(100, 999) # 100-999 (3-digit)
    else:
        # This part should ideally not be reached if get_level() is correct,
        # but it adheres to the function's contract to raise ValueError.
        raise ValueError("Level must be 1, 2, or 3")


if __name__ == "__main__":
    main()
    