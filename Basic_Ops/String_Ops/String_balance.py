# [invalid-name]
def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
print(string_balance_test(s1, s2))

s1 = "Ynf"
s2 = "PYnative"
print(string_balance_test(s1, s2))


# Solution 2
def string_balance(str1, str2):

    for char in str1:
        if char in str2:
            return "balance"
        else:
            return "Not balance"


str1 = input("Enter the string1: ")
str2 = input("Enter the string2: ")
print(string_balance(str1, str2))
