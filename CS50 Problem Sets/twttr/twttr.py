word = input("Input: ")
new = []
for w in word:
    if w not in ["a","e","i","o","u","O","A","E","I","U"]:
        new.append(w)
print(f"Output: {"".join(new)}")
