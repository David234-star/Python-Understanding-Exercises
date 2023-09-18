# Solution 1

str1 = "PYnative"

ch = str1[::-1]

print(ch)

print("--------------------------")
# Solution 2

print("Original String is:", str1)

str1 = ''.join(reversed(str1))
print("Reversed String is:", str1)

