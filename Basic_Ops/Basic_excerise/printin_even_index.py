str = "Ranadeer"
"""
    Even index are:
        R, n, d, e
"""
print("Original String is ", str)
print("Printing only even index chars")
print(str[0::2])


# Solution 1

size = len(str)

for i in range(0, size - 1, 2):
    print("index [", i, "]", str[i])


# Solution 2

for i in str[0::2]:
    print(i)
