def main():
       camel = input("camelCase: ")
       thec = convert(camel)
       print(f"snake_case: {thec}")


def convert(camel):
       capital=[]
       for char in camel:
                if char.isupper():
                    capital.append("_")
                    capital.append(char.lower())
                else:
                    capital.append(char)
       return "".join(capital)


if __name__ == "__main__":
      main()
