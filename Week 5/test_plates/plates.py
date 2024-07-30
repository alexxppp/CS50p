def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (2 <= len(s) <= 6) and (s[0].isalpha() and s[1].isalpha()) and has_continuos_numbers(s) and not has_punctuation(s)


def has_punctuation(s):
    return any(char in string.punctuation for char in s)


def has_continuos_numbers(s):
    for digit in range(2, len(s)):
        if s[digit].isnumeric():
            if s[digit] == "0":
                return False
            elif s[digit:].isnumeric():
                return True
            elif not s[digit:].isnumeric():
                return False
    return True


if __name__ == "__main__":
    main()
