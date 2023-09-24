# Create a Python set such that it shows the element from both lists in a pair
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

print("First list: ", first_list)
print("Second list: ", second_list)

addition = zip(first_list, second_list)

pairofset = set(addition)

print("Combination pairs of tuple in the set format from given list:\n", pairofset)
