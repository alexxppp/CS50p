greeting = input("greeting here: ")

greeting = greeting.lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif greeting[0] == "h" and not greeting.startswith("hello"):
    print("$20")
else:
    print("$100")
