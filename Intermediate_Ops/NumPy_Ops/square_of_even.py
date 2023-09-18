import numpy as np
import math as m

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])
print("addition of two arrays is \n")
addion = arrayOne + arrayTwo
print(addion)

for num in np.nditer(addion, op_flags=['readwrite']):
    num[...] = num * num

print("\nResult array after calculating the square root of all elements\n")
print(addion)
