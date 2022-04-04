import string

text = (input())
text = text.lower()

chars = string.ascii_lowercase
chars = chars + " '’"
for letter in text:
    if letter not in chars:
        text = text.replace(letter, "")

print(text)