def Black_jack(card_1, card_2):
    if card_1 == 'A' or card_2 == 'A':
        return 11
    elif card_1 == 'K' or card_2 == 'K':
        return 10
    elif card_1 == 'Q' or card_2 == 'Q':
        return 10
    elif card_1 == 'J' or card_2 == 'J':
        return 10
    else:
        return card_1 + card_2


print(Black_jack('A', 'K'))
print(Black_jack('A', 'Q'))
print(Black_jack('A', 'J'))
print('------------------------------------------------------------------------------------')
print('                                        and                                         ')
print('------------------------------------------------------------------------------------')
n = int(input("Enter the number: "))

for i in range(1, n+1):
    print('*'*i)

print('-----------------____----------------')

for i in range(1, n+1):
    print(' '*(n-i), '*'*(2*i-1))
