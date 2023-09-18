import numpy as np


# Printing Input Array
# [[11 22 33]
#  [44 55 66]
#  [77 88 99]]

# Printing array of items in the third column from all rows
# [33 66 99]

sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print("Printing Input Array")
print(sampleArray)

items = sampleArray[..., 2]
print("Printing array of items in the third column from all rows ", items)
