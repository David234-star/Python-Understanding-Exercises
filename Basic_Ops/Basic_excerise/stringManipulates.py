# Solution 1

str1, str2, str3 = input("Enter three strings: ").split()
print("Name 1: ", str1)
print("Name 2: ", str2)
print("Name 3: ", str3)

# Solution 2

strs = int(input("Enter the size of the list: "))
strings = []
for i in range(strs):
    name = input("Enter the string: ")
    strings.append(name)
strings = str(strings)
strings = strings[1:-1]

print(strings)
