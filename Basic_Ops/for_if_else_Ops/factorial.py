n = int(input("Enter the number: "))

factorial = 1
for i in range(1, n+1):
    factorial = factorial * i

print(f"The Factorial of {n} is {factorial}")

# Solution 2
num = 5
factorial1 = 1
if num < 0:
    print("Factorial for this number doesn't exist in this universe!")
elif num == 0:
    print("Factorial of 0 is 1 by it's universal definition, Okay!")
else:
    for i in range(1, num + 1):
        factorial1 = factorial1 * i
    print("The Factorial of ", num, "is", factorial1)
