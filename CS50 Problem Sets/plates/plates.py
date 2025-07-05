def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not(len(s) > 1 and len(s) < 7 and s[0:2].isalpha() and "." not in s and " " not in s):
        return False

    found_number = False

    for p in s:
           if p.isdigit():
               if not found_number:
                    if p=="0":
                         return False
                    found_number = True
           else:
              if found_number:
                   return False
    return True


main()
