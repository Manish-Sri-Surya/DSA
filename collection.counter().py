from collections import Counter

# Number of shoes
X = int(input())

# Shoe sizes available
shoe_sizes = list(map(int, input().split()))

# Count each shoe size
shop = Counter(shoe_sizes)

# Number of customers
N = int(input())

money_earned = 0

# Customer purchases
for _ in range(N):
    size, price = map(int, input().split())

    if shop[size] > 0:
        money_earned += price
        shop[size] -= 1

# Output total earnings
print(money_earned)