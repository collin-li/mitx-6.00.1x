# PROBLEM
#
# You'll notice that in Problem 2, your monthly payment had to be a multiple of 
# $10. Why did we make it that way? You can try running your code locally so 
# that the payment can be any dollar and cent amount (in other words, the 
# monthly payment is a multiple of $0.01). Does your code still work? It 
# should, but you may notice that your code runs more slowly, especially in 
# cases with very large balances and interest rates.
#
# Well then, how can we calculate a more accurate fixed monthly payment than 
# we did in Problem 2 without running into the problem of slow code? We can 
# make this program run faster using a technique introduced in lectures - 
# bisection search!
#
# The following variables contain values as described below:
# 1. balance - the outstanding balance on the credit card
# 2. annualInterestRate - annual interest rate as a decimal
#
# To recap the problem: we are searching for the smallest monthly payment such 
# that we can pay off the entire balance within a year. What is a reasonable 
# lower bound for this payment value? $0 is the obvious answer, but you can do 
# better than that. If there was no interest, the debt can be paid off by 
# monthly payments of one-twelth of the original balance, so we must pay at 
# least this much every month. One-twelfth of the original balance is a good 
# upper bound.
#
# What is a good upper bound? Imagine that instead of paying monthly, we paid 
# off the entire balance at the end of the year. What we ultimately pay must be 
# greater than what we would've paid in monthly installments, because the 
# interest was compounded on the balance we didn't pay off each month. So a 
# good upper bound for the monthly payment would be one-twelfth of the balance, 
# after having its interest compounded monthly for an entire year.

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

lower = balance / 12 # Lower bound based on lowest (zero) interest effect
upper = balance * (1 + monthlyInterestRate)**12 / 12  # Upper bound based on highest interest effect (unchecked growth)
monthlyPayment = (lower + upper)/2

testbalance = yearEndBalance(balance, monthlyPayment)

while abs(testbalance) > 0.01: # Error tolerance to the cent (0.01)
    if testbalance > 0: lower = monthlyPayment
    elif testbalance < 0: upper = monthlyPayment
    monthlyPayment = (lower + upper)/2

    testbalance = yearEndBalance(balance, monthlyPayment)

print('Lowest Payment:', round(monthlyPayment,2))
