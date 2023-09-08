# Solution 1
for i in range(6):
    for j in range(i):
        print(i, end=" ")
    print(" ")

# Solution 2
rows = 6
for num in range(rows):
    for k in range(num):
        print("*", end=" ")
    print(" ")

# Solution 3
for num in range(rows):
    for k in range(num):
        print("-", end="")
    print(" ")
