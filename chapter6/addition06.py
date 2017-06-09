'''
Created on Jun 7, 2017

@author: jwang02
'''
'''Display a sum problems with a function returning a string,
not printing directly.
'''

def sumProblemString(x, y):
    sumResult = x + y
    return 'The sum of {} and {} is {}.'.format(x, y, sumResult)

def main():
    print(sumProblemString(7, 5))
    print(sumProblemString(3.45, 3.3))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(sumProblemString(a, b))

main() 
