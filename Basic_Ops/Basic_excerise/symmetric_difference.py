# Symmetric Difference between elements
from collections import Counter
from itertools import chain
A = {1, 2, 4, 5, 6}
B = {3, 5, 6, 7, 8}
C = {8, 9, 0, 10, 15}
D = {18, 19, 20, 10, 15}
# Solution 1

single_iter = chain(A, B, C, D)

Occurence = Counter(single_iter)

sym_diff = set([i for i in Occurence if Occurence[i] == 1])
print(f"Symmetric Difference {sym_diff}")


# Solution 2
print("Symmetric difference is: ", A ^ B ^ C ^ D)


# Solution 3
set2 = A.symmetric_difference(B)
set3 = set2.symmetric_difference(C)
set4 = set3.symmetric_difference(D)

print(f"Symmetric Difference between A,B,C and D: {set4}")

# Solution 4
