
# Solution 1 for known strings
str1 = "Rm"
str2 = "ana"

first = str1[0]
last = str1[1]
x = first + str2

res = x + last

print("New String is:", res)

# Solution 2
# Unknown strings that is we don't how they are like


def append_middle(s1, s2):
    print("Original Strings are", s1, s2)

    # middle index number of s1
    mi = int(len(s1) / 2)

    # get character from 0 to the middle index number from s1
    x = s1[:mi:]
    # concatenate s2 to it
    x = x + s2
    # append remaining character from s1
    x = x + s1[mi:]
    print("After appending new string in middle:", x)


f = input("Enter the String: ")
l = input("Enter the String: ")
append_middle(f, l)
