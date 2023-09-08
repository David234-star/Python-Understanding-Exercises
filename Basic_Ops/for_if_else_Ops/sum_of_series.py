# Solution 1
n = 5

# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    # adding up the start to current sum_seq
    sum_seq += start
    # updating the start variable to continue the process
    start = (start * 10) + 2

print(end="=")

print("\nSum of sequence for the given is", sum_seq)
