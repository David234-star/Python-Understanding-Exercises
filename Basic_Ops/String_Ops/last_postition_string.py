str1 = "Emma is a data scientist who knows Python. Emma works at google."
ch = input("Enter the String: ")
print("Last Occurence of string is: ",str1.rfind(ch))

# Spliting the string using split() method

str1 = "Emma-is-a-data-scientist"

ch1 = str1.split("-")

print("Displaying substring: ")
for sub in ch1:
    print(sub)
