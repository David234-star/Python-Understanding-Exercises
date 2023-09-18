import string

str1 = '/*Jon is @developer & musician!!'

print("Original string: ",str1)

replace_str = "#"

for char in string.punctuation:
    str1 = str1.replace(char,replace_str)
print("After string replacement: ",str1)