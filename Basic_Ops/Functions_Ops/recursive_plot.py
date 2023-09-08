def recursivefunc(num):  # defining the function for addtion of 0 to 10 numbers
    if num:  # if there is a number then this will be executed
        return num + recursivefunc(num - 1)  # calling itself again and again
    else:  # if there is no number then this will be executed
        return 0  # returning 0


result = recursivefunc(10)  # calling the function
print(result)  # output the result to the command prompt
