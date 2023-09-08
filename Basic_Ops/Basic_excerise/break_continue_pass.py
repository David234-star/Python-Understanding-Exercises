# break statement
i = int(input(" Enter the number: "))
for n in range(2, i):
    for x in range(2, n):
        # checking the condition where to break the iteration, it is necessary for the break(conditio is necessary)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break

    else:  # loop fell through without finding a factor
        print(n, 'is the prime number')

print("---------------------------___--------------------------")

# continue statement
for n in range(2, i):
    if n % 2 == 0:
        print(n, "is even number")
        continue
    print(n, "is odd number")

print("---------------------------___--------------------------")

while True:
    pass  # pass do nothing, It can be used when a statement is required syntactically but the program requires no action

print("Nothing done in while loop")
