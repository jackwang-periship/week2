'''
Created on Jun 7, 2017

@author: jwang02
'''

def sumProblem(x, y):
    sumResult = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sumResult)
    print(sentence)

def main():
    sumProblem(4, 9)
    sumProblem(7.89, 4.01)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)
#     print(sumProblem(a, b))

main() 
