# Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"

sub_string = "USA"

temp_str = str1.lower()


occurr = temp_str.count(sub_string.lower())

print("The count of {} is: ".format(sub_string), occurr)


# Solution 2 - finding unknown string occurence until user input have given

# def user_input_occurence(str2):
