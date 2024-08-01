from validator_collection import checkers


def main():
    if checkers.is_email(input("email here: ")):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
