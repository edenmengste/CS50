import emoji

inp = input("Input: ")

emo = emoji.emojize(inp, language="en")
print(f"Output: {emo}")
