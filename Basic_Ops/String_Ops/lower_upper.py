str1 = "PyNaTive"
lower = []
upper = []
# iterating through the str1
for char in str1:
    # checking the char is lower or not
    if char.islower():
        lower.append(char)
    # checking the char is upper or not
    else:
        upper.append(char)

# joining the lower and upper case one after other
sorted_list = ''.join(lower+upper)
print(sorted_list)
