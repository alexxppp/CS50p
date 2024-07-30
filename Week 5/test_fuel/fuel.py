def main():
    fraction = input("fraction here: ")

    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except:
        print("Error")


def convert(fraction):
    try:
        numerator, denominator = int(fraction.split("/")[0]), int(fraction.split("/")[1])
        return round(numerator / denominator * 100)
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
