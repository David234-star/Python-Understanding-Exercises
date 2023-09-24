l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

lsf = l1[1::2]  # Odd index first list
lss = l2[0::2]  # even index second list
print(lsf)
print(lss)

print("Combination of two lists is: ")
print(lsf+lss)
