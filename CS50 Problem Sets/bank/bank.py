greet =input("Greeting: ")
if "hello" in greet.strip().lower():
    print("$0")
elif greet[0].strip().lower() == "h":
    print("$20")
else:
    print("$100")
