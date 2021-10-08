income = float(input("Enter the annual income: "))

#
# Write your code here.
#
# if the citizen's income was not higher than 85,528 thalers
# the tax was equal to 18% of the income minus 556 thalers and 2 cents 

tax = 0
if income < 85528:
    calc = ((income*18)/100) - 556.2
    tax = calc
    print('went here')

# if the income was higher than this amount, the tax was equal to 14,839 thalers
# and 2 cents, plus 32% of the surplus over 85,528 thalers.
elif income > 85528:
    calc = (((income-85528)*32)/100) + 14839.2
    tax = calc

tax = round(tax, 0)

# If the calculated tax is less than zero, 
# it only means no tax at all (the tax is equal to zero). 

if tax < 0:
    tax = 0.0
    
print("The tax is:", tax, "thalers")
