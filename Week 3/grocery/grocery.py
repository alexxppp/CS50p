grocery_list = {}

while True:
    try:
        item = input()
        # Update the count of the item in the dictionary
        grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        print()
        # Sort the dictionary by item names
        sorted_items = sorted(grocery_list.items())
        count = 1
        for item, quantity in sorted_items:
            print(f"{quantity} {item.upper()}")
            count += 1
        break
