import sys
import os

if len(sys.argv) != 2:
    sys.exit(1)
elif not sys.argv[1].endswith(".py"):
    sys.exit(1)
elif not os.path.exists(sys.argv[1]):
    sys.exit(1)

lines = 0
with open(sys.argv[1]) as file:
    for line in file:
        if line.strip().startswith("#"):
            continue
        if line.strip() == "":
            continue
        lines += 1

print(lines)
