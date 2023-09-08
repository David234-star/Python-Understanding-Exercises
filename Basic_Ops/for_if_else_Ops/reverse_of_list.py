# Solution 1
list1 = [10, 20, 30, 40, 50, 60]
newlist = reversed(list1)

for item in newlist:
    print(item)


# Solution 2
print("==")
size = len(list1)
for item in range(size-1, -1, -1):
    print(list1[item])
