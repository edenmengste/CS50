import sys

def main():
    word = ""
    try:
        word = input()
    except EOFError:
        pass
    shortened_word_list = shorten(word)
    print("".join(shortened_word_list))
    sys.exit(0)

def shorten(word):
    result_chars = []
    for char in word:
      if char.lower() not in ["a","e","i","o","u"]:
        result_chars.append(char) 
    return "".join(result_chars)

if __name__ == "__main__":
    main()
