# Solution 1
str1 = "PYranadeer29@#8496"

total = 0
cnt = 0

for char in str1:
    if char.isdigit():
        total += int(char)
        cnt += 1

aver = total / cnt
print(f"Sum is: {total} Average is  {aver}")

# Solution 2
import re
input_str = "PYranadeer29@#8496"

digit_list = [int(num) for num in re.findall(r'\d',input_str)]
print("Digits list",digit_list)

total1 = sum(digit_list)

aver1 = total / len(digit_list)

print(f"Sum is: {total1} Average is  {aver1}")
