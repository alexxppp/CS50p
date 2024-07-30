import sys
import os
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    sys.exit(1)
elif not os.path.exists(sys.argv[1]):
    sys.exit(1)

try:
    with open(sys.argv[1], newline="") as file:
        reader = csv.reader(file)
        item_list = list(reader)
        rows = len(item_list)
        if rows != 6:
            sys.exit(1)
        columns = len(item_list[0])
        if columns != 3:
            sys.exit(1)
except:
    print("Error while opening the csv file")

print(tabulate(item_list, tablefmt="grid", headers="firstrow"))
