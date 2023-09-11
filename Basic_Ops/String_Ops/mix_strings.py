def mix_strings(s1, s2):
    first_char = s1[0]+s2[0]

    # getting the middle character of both strings
    middle_char = s1[int(len(s1)/2):int(len(s1)/2)+1] + \
        s2[int(len(s2)/2): int(len(s2)/2)+1]

    # getting last char from both strings

    last_char = s1[-1]+s2[-1]

    result = first_char + middle_char + last_char

    return result


a = "America"
b = "Japan"
print("The mixed string is: ", mix_strings(a, b))
