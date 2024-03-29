# Solution: 1
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result_list = []
# iterate through list1
for num in list1:
    if num % 2 != 0:  # Checking for the odd numbers
        result_list.append(num)
# iterate through list2
for num in list2:
    if num % 2 == 0:  # Checking for the even numbers
        result_list.append(num)

print(result_list)  # output the odd and even numbers

# Solution: 2


def merge_list(list1, list2):
    result_list = []

    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to result list
            result_list.append(num)

    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            # add even number to result list
            result_list.append(num)
    return result_list


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))
