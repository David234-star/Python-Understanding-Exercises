# Solution 1
numbers = []  # initiation of list to numbers
n = int(input("Enter the size of the list"))  # size of the list
# run the loop n times as per the user input
for i in range(n):
    # accept the user input
    digit = float(input(f"Enter the number at location {i}: "))
    numbers.append(digit)  # adding the number to the list

print(numbers)  # output the list that we got from the iteration


# Solution 2
numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)
