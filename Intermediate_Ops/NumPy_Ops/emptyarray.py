import numpy as np

firstArray = np.empty([4, 2], dtype=np.uint16)

print("Printing array attributes")

print("Array Shape is: ", firstArray.shape)
print("Array dimensions are ", firstArray.ndim)
print("Length of each element of array in bytes is  ", firstArray.itemsize)
# print(dir(np))
