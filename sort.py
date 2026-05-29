s = input()

lower = sorted([i for i in s if i.islower()])
upper = sorted([i for i in s if i.isupper()])
odd = sorted([i for i in s if i.isdigit() and int(i) % 2 != 0])
even = sorted([i for i in s if i.isdigit() and int(i) % 2 == 0])

print("".join(lower + upper + odd + even))