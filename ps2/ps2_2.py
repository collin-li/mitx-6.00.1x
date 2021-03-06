# PROBLEM
#
# Now write a program that calculates the minimum fixed monthly payment needed 
# in order to pay off a credit card balance within 12 months. By a fixed 
# monthly payment, we mean a single number which does not change each month, 
# but instead is a constant amount that will be paid each month.
#
# In this problem, we will not be dealing with a minimum monthly payment rate.
# 
# The following variables contain values as described below:
# 1. balance - the outstanding balance on the credit card
# 2. annualInterestRate - annual interest rate as a decimal
#
# The program should print out one line: the lowest monthly payment that will 
# pay off all debt in under 1 year, for example:
#
# 'Lowest Payment: 180'
#
# Assume that the interest is compounded monthly according to the balance at 
# the end of the month (after the payment for that month is made). The monthly 
# payment must be a multiple of $10 and is the same for all months. Notice 
# that it is possible for the balance to become negative using this payment 
# scheme, which is okay.

# For test purposes
balance = 5000
annualInterestRate = 0.18

# SOLUTION 
def yearEndBalance(balance, monthlyPayment):
    '''
    balance: outstanding balance on the credit card (int or float)
    monthlyPayment: fixed monthly payment (int or float)
    
    returns: ending balance on the credit card after 12 months (int or float)
    '''
    for month in range(12):
        balance = (balance - monthlyPayment) * (1 + monthlyInterestRate)
    return balance

monthlyInterestRate = annualInterestRate / 12.0

monthlyPayment = 10*int(balance/12/10) # Initial guess set as 1/12th of balance

while yearEndBalance(balance, monthlyPayment) > 0:
    monthlyPayment += 10

print('Lowest Payment:', monthlyPayment)    
