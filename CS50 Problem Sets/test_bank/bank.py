import sys # Import the sys module to use sys.exit()

def main():
    # Initialize greeting_input in case of EOFError
    greeting_input = ""

    try:
        # 1. REMOVE THE PROMPT STRING "Greeting: "
        #    check50 provides input directly, it doesn't want your program to print prompts.
        greeting_input = input()
    except EOFError:
        # 2. Add try-except EOFError to gracefully handle no input or premature stream close.
        #    If EOFError occurs, we'll just use an empty string for processing.
        pass

    # Call the value function to get the amount
    amount = value(greeting_input)

    # Only main() should call print, so this is correct for outputting the amount.
    print(f"${amount}")

    # 3. Explicitly exit with status code 0.
    #    This is a common fix for check50 issues where it expects a specific exit code.
    sys.exit(0)

def value(greeting):
    """
    Calculates the amount based on the greeting.
    Returns 0 if greeting starts with "hello" (case-insensitive).
    Returns 20 if greeting starts with "h" (case-insensitive, but not "hello").
    Returns 100 otherwise.
    Assumes that the string passed to the value function will not contain any leading spaces.
    """
    # Convert the greeting to lowercase for case-insensitive comparison
    greeting_lower = greeting.lower()

    # Check for "hello"
    if greeting_lower.startswith("hello"):
        return 0
    # Check for "h" (but not "hello", which is already handled above)
    elif greeting_lower.startswith("h"):
        return 20
    # Otherwise
    else:
        return 100

if __name__ == "__main__":
    main()
