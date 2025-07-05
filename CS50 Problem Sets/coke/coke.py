due = 50
while due > 0:
    print(f"Amount Due: {due}")
    insert = input("Insert Coin: ")
    if insert in ["25","10","5"]:
       due -= int(insert)
if due <= 0:
           print(f"Change Owed: {due*-1}")

