rows = 5
for i in range(0, rows):  # it will take care of the rows(0 through 5)
    # it will take care of columns(0 through what value that the i have right now + 1)
    for j in range(0, i + 1):
        # if it i=1 then it will print i+1 = 1+1 = 2 likewise
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):  # here it will come from 5 through 0 and reducing the rows to -1
    for j in range(0, i - 1):  # here it will come 0 through i - 1 i.e., 0,present of i - 1 = 5 - 1 = 4
        print("*", end=' ')
    print("\r")  # carrieage return operator
