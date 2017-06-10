'''
Created on Jun 9, 2017

@author: student
'''
def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    balance = newBalance

def test():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print amount
    
test()
