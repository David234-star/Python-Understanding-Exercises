# this is the symbols, characters, and alphbets counts program
def counting(string1):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in string1:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    print("Chars= ", char_count, "\nDigits= ",
          digit_count, "\nSymbols= ", symbol_count)


sample_one = input("Enter the strings: ")
counting(sample_one)
