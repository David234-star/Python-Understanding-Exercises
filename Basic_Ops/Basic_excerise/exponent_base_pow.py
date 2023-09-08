# Solution 1
from math import pow


def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)


bas = int(input("Enter the base number: "))
expo = int(input("Enter the exponent number: "))

exponent(bas, expo)

# Solution 2
print("The required result: ", pow(bas, expo))

# Solution 3
print("The required result: ", bas**expo)
