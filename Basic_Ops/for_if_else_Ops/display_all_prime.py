# Solution 1
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)

# Solution 2


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Find prime numbers between 25 and 50
lower_limit = 25
upper_limit = 50

print(f"Prime numbers between {lower_limit} and {upper_limit} are:")
for num in range(lower_limit, upper_limit + 1):
    if is_prime(num):
        print(num)

# Solution 3
print("Prime numbers from", start, "to", end, "are: ")
for item in range(start, end+1):
    if item > 1:
        for i in range(2, item):
            # check for factors
            if (item % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(item)
