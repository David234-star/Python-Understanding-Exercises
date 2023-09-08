def is_valid_parentheses(s):  # using stack we can implement this
    stack = []

    for char in s:
        if char == '(':  # Checking whether the given input is parentheses
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':  # if the given input is not parenthesis it will return false
                return False
            stack.pop()

    return len(stack) == 0


print(
    "----------------------Validation for parentheses, whether they are in correct structure or not----------------------")
# Get the number of test cases from the user
test_cases = int(input("Enter the number of test cases: "))

# Process each test case
for _ in range(test_cases):
    print("-----")
    # Get the input parentheses string from the user
    parentheses_string = input("Enter the parentheses string: ")

    # Check if the parentheses are balanced and valid
    result = is_valid_parentheses(parentheses_string)

    # Print the result
    print(result)
