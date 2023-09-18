# Solution 1
s1 = "Abc"
s2 = "Xyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

# Solution 2


def random_stringplace(a, b):
    length1 = len(a)
    length2 = len(b)
    # getting the length of bigger string
    len_str = length1 if length1 > length2 else length2
    # initializing the result varible
    res = ""
    # reverse the string
    # b = b[::-1]

    # iterating the string
    # a ascending and b is descending
    for i in range(len_str):
        if i < length1:
            res = res + a[i]
        if i < length2:
            res = res + b[i]
    return res


str1 = input("Enter the string1: ")
str2 = input("Enter the string2: ")

print(random_stringplace(str1, str2))
