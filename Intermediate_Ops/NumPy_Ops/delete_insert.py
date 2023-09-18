# Delete the second column from a given array and insert the following new column in its place.

import numpy as np

print("Original Array")
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
newColumn = np.array([[10, 10, 10]])
print(sampleArray)

print("Array after deleting column 2 on axis 1")
sampleArray = np.delete(sampleArray, 1, axis=1)
print(sampleArray)

print("Array after inserting column 2 on axis 1")
sampleArray = np.insert(sampleArray, 1, newColumn, axis=1)
print(sampleArray)
