# PROBLEM
#
# Write a program to calculate the credit card balance after one year if a 
# person only pays the minimum monthly payment required by the credit card 
# company each month.
#
# The following variables contain values as described below:
# 1. balance - the outstanding balance on the credit card
# 2. annualInterestRate - annual interest rate as a decimal
# 3. monthlyPaymentRate - minimum monthly payment rate as a decimal
#
# For each month, calculate statements on the monthly payment and remaining 
# balance. At the end of 12 months, print out the remaining balance. Be sure 
# to print out no more than two decimal digits of accuracy.
    
# For test purposes
balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

# SOLUTION
monthlyInterestRate = annualInterestRate / 12.0

for month in range(12):
    monthlyPayment = monthlyPaymentRate * balance
    balance = (balance - monthlyPayment) * (1 + monthlyInterestRate)

print('Remaining balance:', round(balance,2))
