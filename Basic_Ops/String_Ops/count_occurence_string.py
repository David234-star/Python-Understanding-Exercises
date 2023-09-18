# Solution 1
str1 = "Apple"

required = dict()

for ch in str1:
    cnt = str1.count(ch)

    required[ch] = cnt

print(required)


# Solution 2

req = {ch: str1.count(ch) for ch in str1}
print(req)



