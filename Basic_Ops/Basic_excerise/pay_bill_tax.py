# Taxable Income	Rate (in %)
# First $10,000	        0
# Next $10,000	        10
# The remaining	        20
# Above is the example one to take the interests based the income

# Solution 1
def income_tax(tax_payable):
    income = 45000
    print("Given income", income)

    if income <= 10000:
        tax_payable = 0
    elif income <= 20000:
        # no tax on first 10,000
        no_tax = income - 10000
        # 10% tax
        tax_payable = no_tax * 10 / 100
    else:
        # first 10,000
        tax_payable = 0

        # next 10,000 10% tax
        tax_payable = 10000 * 10 / 100

        # remaining 20% tax
        tax_payable += (income - 20000) * 20 / 100
    return tax_payable


print("Total tax to pay is", income_tax(0))

# Solution 2:
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)
