amount = 50
accepted = [5, 10, 25]

while amount > 0:
    inserted = int(input("inserted amount here:"))
    if inserted in accepted:
        amount -= inserted
    if not amount <= 0:
        print("Amount Due:", amount)

print("Change Owed:", abs(amount))
