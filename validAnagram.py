from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

# Input
s = input("Enter first string: ")
t = input("Enter second string: ")

# Object creation
obj = Solution()

# Function call
result = obj.isAnagram(s, t)

# Output
print(result)