vowels = ["a", "e", "i", "o", "u"]

word = input("string here: ")

shortened_word = ""

for letter in word:
    if not letter.lower() in vowels:
        shortened_word += letter

print(shortened_word)
