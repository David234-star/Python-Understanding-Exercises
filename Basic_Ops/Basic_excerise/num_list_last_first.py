def list_out_last_first(num1):
    print("Original List: ", num1)

    first_element = num1[0]
    last_element = num1[-1]

    if first_element == last_element:
        print(first_element, last_element)
        return True
    else:
        print(first_element, last_element)
        return False


list1 = [2, 3, 4, 5, 6, 7, 2]
print(list_out_last_first(list1))

list2 = [2, 3, 4, 5, 6, 7]

print(list_out_last_first(list2))
