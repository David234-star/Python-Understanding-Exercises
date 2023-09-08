# Solution 1
str1 = "Ranam"
print("Original string is:", str1)
# get the first element of string
result = str1[0]

# adding the first element and middle element of string
result = result + str1[len(str1)//2]

# adding up the result to last element and
# getting the final string which contains first, middle and last elements
result = result + str1[len(str1)-1]

# printing the result which is final string
print("New string is:", result)


# Solution 2

str1 = 'Ranam'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)

# Solution 3
