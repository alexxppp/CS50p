def question():
    fraction = input("fraction here: ")
    if "/" not in fraction:
        question()
        return

    fraction = fraction.split("/")

    try:
        numerator, denominator = int(fraction[0]), int(fraction[1])
        if numerator > denominator:
            question()
            return
        percentage = round(numerator / denominator * 100)
    except (ValueError, ZeroDivisionError):
        question()
        return

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


question()
