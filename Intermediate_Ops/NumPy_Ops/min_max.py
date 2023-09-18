import numpy as np

print("Original Array")
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)

print("Printing amin Of Axis 1")
miniofaxis1 = np.amin(sampleArray, 1)
print(miniofaxis1)

print("Printing amax Of Axis 0")
maxiofaxis0 = np.amax(sampleArray, 0)
print(maxiofaxis0)
