num = int(input("Enter the number: "))
count = 0
while num != 0:
    num = num//10
    count = count + 1
print("Total no of digits are: ", count)
