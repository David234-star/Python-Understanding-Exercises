def product(num1, num2):
    pro = num1 * num2
    summ = num1 + num2

    if (pro <= 1000):
        return pro
    else:
        return summ


result = product(100, 500)
print("The result is ", result)

result = product(40, 30)
print("The result is ", result)

result = product(30, 10)
print(result)
