str1 = 'I am 25 years and 10 months old'
sum1 = ""
for ch in str1:
    if ch.isdigit():
        sum1 += ch
print(sum1)

# Solution 2

ch2 = "".join([item for item in str1 if item.isdigit()])
print(ch2)