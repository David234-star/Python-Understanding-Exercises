num1 = 0
num2 = 1
print("Fibonacci Sequence: ")
for i in range(10):  # iterates 10 times
    print(num1, end="  ")  # prints initial number

    # adding first number to next number which occurs in fibonacci series
    res = num1 + num2
    # update the first number with next number
    num1 = num2
    # updating the next number with another next number
    num2 = res
