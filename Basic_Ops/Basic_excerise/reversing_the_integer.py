num = int(input("Enter the number: "))
print("Given number: ", num)

while num > 0:
    # get the number which is last digit
    dig = num % 10
    # remove the last number from given number
    num = num // 10
    print(dig, end=" ")


# num = int(input("Enter the number: "))

# digit = list(num)  # type: ignore
# for i in digit:
#     if i > 0:
#         digit = digit % 10  # type: ignore
#         print(digit) # How to rectify the errors in the list, why integers are not iterable in this context, we have to check that one
