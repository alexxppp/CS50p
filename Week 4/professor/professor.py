import random

levels = [1, 2, 3]


def main():
    level = get_level()

    questions = []
    answers = []
    for _ in range(10):
        first = generate_integer(level)
        second = generate_integer(level)
        questions.append(f"{first} + {second} = ")
        answers.append(first + second)

    count = 0
    correct = 0
    while count < 10:
        mistakes = 0
        while mistakes < 3:
            answer = input(questions[count])

            if is_integer(answer) and int(answer) == answers[count]:
                correct += 1
                break
            else:
                print("EEE")
                mistakes += 1

        if mistakes == 3:
            print(f"{questions[count]}{answers[count]}")

        count += 1

    print(f"Score: {correct}")


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in levels:
                continue
            return level
        except:
            continue


def generate_integer(level):
    if level not in levels:
        raise ValueError
    if level == 1:
        return random.randrange(0, pow(10, level))
    return random.randrange(pow(10, (level - 1)), pow(10, level))


if __name__ == "__main__":
    main()
