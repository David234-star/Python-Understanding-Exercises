row = int(input("Enter the number: "))
# Solution 1
for i in range(row, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print(" ")

# Solution 2
