numbers = input().split()
answers = input().split()

nums = set()
ans = set()
for number in numbers:
    nums.add(number)
for answer in answers:
    ans.add(answer)

if nums == ans:
    print("True")
else:
    print("False")