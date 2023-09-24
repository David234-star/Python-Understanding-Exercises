sampleList = [34, 54, 67, 89, 11, 43, 94]
print("Original List: ", sampleList)

element = sampleList.pop(4)
print("Removing element at index 4: ", sampleList)

sampleList.insert(2, element)
print("Inserting the element at index 2: ", sampleList)

sampleList.append(element)
print("After inserting the element at last position: ", sampleList)
