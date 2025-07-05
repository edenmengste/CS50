import sys 

def main():
    greeting_input = ""

    try:
        greeting_input = input()
    except EOFError:
        pass
    amount = value(greeting_input)
    print(f"${amount}")
    sys.exit(0)

def value(greeting):
    greeting_lower = greeting.lower()
    if greeting_lower.startswith("hello"):
        return 0
    elif greeting_lower.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
