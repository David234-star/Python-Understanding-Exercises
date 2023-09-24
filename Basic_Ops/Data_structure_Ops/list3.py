sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list:", sample_list)

count_list = dict()

for item in sample_list:
    if item in count_list:
        count_list[item] += 1
    else:
        count_list[item] = 1

print("Counted items in list given above: ", count_list)
