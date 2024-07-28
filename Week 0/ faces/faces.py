def convert(text):
    newtext = text.replace(":)", "🙂")
    newtext = newtext.replace(":(", "🙁")
    return newtext


def main():
    text = input("text here: ")
    print(convert(text))


if __name__ == "__main__":
    main()
