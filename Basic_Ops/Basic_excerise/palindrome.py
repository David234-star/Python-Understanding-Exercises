# Solution 1 : integer reversal

def palindrome(number):
    print("Original number: ", number)
    original_num = number

    reverse_num = 0
    while number > 0:
        remainder = number % 10
        reverse_num = (reverse_num * 10) + remainder
        number = number // 10

    if original_num == reverse_num:
        print("Given number is palindrome")
    else:
        print("Given number is not the palindrome")


palindrome(121)
palindrome(125)
palindrome(111)

# Solution 2:String Comparison


def is_palindrome_string_comparison(number):
    print("original number", number)
    num_str = str(number)
    if num_str == num_str[::-1]:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")


# Solution 3: Using Lists


def is_palindrome_using_lists(number):
    print("original number", number)
    num_str = str(number)
    digit_list = [int(digit) for digit in num_str]
    reversed_list = digit_list[::-1]
    if digit_list == reversed_list:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")


# Test cases
is_palindrome_string_comparison(125)
is_palindrome_using_lists(125)
