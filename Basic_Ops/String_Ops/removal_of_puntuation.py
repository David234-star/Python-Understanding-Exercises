# Solution 1
import string

str1 = "/*Jon is @developer & musician"
print("Original String is: ", str1)

ster = str1.translate(str.maketrans('', '', string.punctuation))
print("After removing punctuation:",ster)

# Solution 2
import re

str2 = re.sub(r'[^\w\s]','',str1)
print(str2)