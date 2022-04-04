import random


# work with this variable
n = int(input())

random.seed(n)

word = "Voldemort"

print(word[random.randrange(0, len(word))])