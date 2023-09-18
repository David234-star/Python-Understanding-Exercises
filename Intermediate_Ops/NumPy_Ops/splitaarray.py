import numpy as np

print("Creating 8X3 array using numpy.arange")
sampleArray = np.arange(10, 34, 1)
sampleArray = sampleArray.reshape([8, 3])

print(sampleArray)

print("\nDividing 8X3 array into 4 sub array\n")
resultArray = np.split(sampleArray, 4)
print(resultArray)
