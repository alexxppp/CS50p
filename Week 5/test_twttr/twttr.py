def main():
    word = input("string here: ")
    print(shorten(word))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    shortened_word = ""
    for letter in word:
        if not letter.lower() in vowels:
            shortened_word += letter
    return shortened_word


if __name__ == "__main__":
    main()
