list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]

print("Original List: ", list1)

length = len(list1)
chunk_size = int(length/3)
start = 0
end = chunk_size

for i in range(3):

    indexs = slice(start, end)

    list_chunk = list1[indexs]

    print("Chunk ", i, list_chunk)

    # reverse the chunk
    print("After reversing it:", list(reversed(list_chunk)))

    start = end
    end += chunk_size
