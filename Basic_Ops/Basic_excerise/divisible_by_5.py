# Solution 1
def divisible_by_5(num):
    print("Original list", num)
    divibility = []
    for fivedivisible in num:
        if fivedivisible % 5 == 0:
            print("Divible by 5: ", fivedivisible)
            divibility.append(fivedivisible)
    return divibility


list1 = [10, 15, 13, 20, 14, 17, 19, 35, 36, 40]
print(divisible_by_5(list1))

# Solution 2( two possibilities)

num_list = [10, 15, 13, 20, 14, 17, 19, 35, 36, 40]
print("Original list", num_list)
# List comprehension POV
print("Divisible by 5: ", [num for num in num_list if num % 5 == 0])

for num in num_list:
    if num % 5 == 0:
        print(num)
