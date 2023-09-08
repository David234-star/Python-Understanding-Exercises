def fib(n):  # Function for the fibinacci series
    a, b = 0, 1
    while a < n:
        # Printing out space b/w digits of fibinacci series
        print(a, end='')
        a, b = b, a+b  # here it will add the first two elements and assign it to the variable
    print()


fib(2000)  # calling the function

print("---------------------------_____________---------------------------")

# defining the function for fibinacci series which print it in list
a = int(input(" Enter your own number: "))


def fib1(n):
    result = []
    a, b = 0, 1
    while a < n:
        # printing out list of fibinacci values
        result.append(a)
        a, b = b, a+b

    return result


fibi = fib1(a)
print(fibi)
