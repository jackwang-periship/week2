'''
Created on Jun 9, 2017

@author: student
'''
#    A program to average a set of numbers
#    Illustrates sentinel loop using negative input as sentinel

def main():
    my_sum = 0.0
    count = 0
    x = input("Enter a number (negative to quit) >> ")
    while x >= 0:
        my_sum = my_sum + x
        count = count + 1
        x = input("Enter a number (negative to quit) >> ")
    print "\nThe average of the numbers is", my_sum / count

main()
