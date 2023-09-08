# Solution 1
num = int(input("Enter the number: "))

print("Given number is: ", num)
print("Reversed number is: ")
while num > 0:
    dig = num % 10
    num = num // 10
    print(dig, end="")
print("\n=======================")

# Solution 2
num1 = int(input("Enter the number: "))
reverse_number = 0
print("Given Number ", num1)
while num1 > 0:
    reminder = num1 % 10
    reverse_number = (reverse_number * 10) + reminder
    num1 = num1 // 10
print("Revere Number ", reverse_number)
