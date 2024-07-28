names = []

while True:
    try:
        name = input("name: ")
        names.append(name)
    except EOFError:
        print()
        break

output = "Adieu, adieu, to"

for name in names:
    if len(names) == 1:
        output += f" {name}"
        break
    elif len(names) == 2:
        output += f" {name} and {names[1]}"
        break
    output += f" {name},"
    if name == names[len(names) - 2]:
        output += f" and {names[len(names) - 1]}"
        break

print(output)
