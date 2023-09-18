import numpy as np

sampleArray = np.array([[3, 6, 9, 12], [15, 18, 21, 24],
                        [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])

print("Printing Input Array")
print(sampleArray)

items = sampleArray[::2, 1::2]

print("Printing array of odd rows and even columns")
print(items)
