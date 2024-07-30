def main():
    print(value(input("greeting: ")))


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting[0] == "h" and not greeting.startswith("hello"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
