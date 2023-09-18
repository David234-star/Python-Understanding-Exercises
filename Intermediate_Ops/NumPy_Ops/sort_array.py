import numpy as np

print("Original Array")
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)

sortbyrow = sampleArray[:, sampleArray[1, :].argsort()]
print("Sorting Original array by second row")
print(sortbyrow)

sortbycolumn = sampleArray[sampleArray[:, 1].argsort()]
print("Sorting Original array by second column")
print(sortbycolumn)
