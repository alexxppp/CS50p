expression = input("expression here: ")

splitted = expression.split(" ")

x, y, z = float(splitted[0]), splitted[1], float(splitted[2])

if y == "+":
    print(f"{(x + z):.1f}")
elif y == "-":
    print(f"{(x - z):.1f}")
elif y == "*":
    print(f"{(x * z):.1f}")
elif y == "/":
    print(f"{(x / z):.1f}")
else:
    print("invalid arithmetic symbol")
