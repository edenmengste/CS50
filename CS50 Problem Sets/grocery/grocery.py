from collections import Counter
grocery_list = Counter()

while True:
    try:
      things= input()
      item = things.upper().strip()
      if item:
         grocery_list[item] += 1


    except EOFError:
        print()
        break

sorted_grocery = sorted(grocery_list.items())

for item_name, Count in sorted_grocery:
   print(f"{Count} {item_name}")
