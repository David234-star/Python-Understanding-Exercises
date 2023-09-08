def sum_even_numbers(number_s):
    even_sum = 0  # initializing the even_sum variable
    even_numbers = []  # creating the list for storing the input values
    for num in number_s:  # iterating the numbers in the list which is under sum_even_numbers
        if num % 2 == 0:
            even_sum += num
            even_numbers.append(str(num))
    even_numbers_str = ' + '.join(even_numbers)
    output = f"Output: {even_sum} (sum of even numbers: {even_numbers_str} = {even_sum})"
    return output


# Getting the number of test cases from the user
test_cases = int(input("Enter the number of test cases: "))

# Processing each test case
for _ in range(test_cases):
    print("-----")
    # Getting the numbers for the current test case
    input_str = input("Input: ")
    numbers = list(map(int, input_str[1:-1].split(',')))

    # Calculating the sum of even numbers and generating the output
    result = sum_even_numbers(numbers)
    print(result)
