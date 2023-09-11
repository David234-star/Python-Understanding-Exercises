# General Example
"""
    Module providingFunction printing python version.
"""
import re
data = input("Enter the your email")
atpos = data.find('@')
print(atpos)

sppos = data.find(' ')
print(sppos)

host = data[atpos+1: sppos]
print(host)


# Regular expression example


email = input("Enter your email> ")

y = re.findall('@([^ ]*)', email)
print(y, "is the host of the given email")
