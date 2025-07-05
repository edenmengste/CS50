def main():
    text = input()
    convert(text)

def convert(text):
    if ':)' or ':(' in text:
        print(text.replace(':)', '🙂').replace(':(', '🙁'))


main()
