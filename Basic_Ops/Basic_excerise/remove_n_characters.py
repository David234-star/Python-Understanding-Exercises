
def remove_chars(user, n):
    print("Original word: ", user)
    x = user[n:]
    return x


print("After the removing the required n characters")
print(remove_chars("Ranadeer", 4))
print(remove_chars("ChandraBose", 6))
print(remove_chars("KamalBasha", 5))
