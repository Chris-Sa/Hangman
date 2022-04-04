

text = input()

start = text.find("old")
end = abs(text.rfind("old"))

print(max(start, end))

