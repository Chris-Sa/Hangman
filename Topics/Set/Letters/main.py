word = input()  # the input word

unique = set()
for letter in word:
    unique.add(letter)

print(len(unique))