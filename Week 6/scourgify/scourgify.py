import sys
import os
import csv


if len(sys.argv) != 3:
    sys.exit("1")

inp, out = sys.argv[1], sys.argv[2]

if not inp.endswith(".csv") or not out.endswith(".csv"):
    sys.exit(1)

if not os.path.exists(inp):
    sys.exit(1)

content = []
try:
    with open(inp, newline="") as inp:
        reader = csv.DictReader(inp)
        for row in reader:
            last, first = row["name"].rstrip().split(", ")
            content.append({"first": first, "last": last, "house": row["house"]})

    with open(out, "w", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["first", "last", "house"])
        for row in content:
            writer.writerow([row["first"], row["last"], row["house"]])

except Exception as e:
    print(e)
