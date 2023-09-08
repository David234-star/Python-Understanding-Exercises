# Getting middle three characters

# Solution 1
def get_middle_chars(str1):
    print("Original String is:", str1)

    # get the middle character
    mid = len(str1)//2

    res = str1[mid-1:mid+2]

    print("Three character string is:", res)


get_middle_chars("Ranamra")
get_middle_chars("davidranadeer")
