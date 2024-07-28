import random

while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
    except ValueError:
        pass

rdm = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess > rdm:
            print("Too large!")
        elif guess < rdm:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
