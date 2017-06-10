'''
Created on Jun 9, 2017

@author: student
'''
#    A program to average a set of numbers
#    Illustrates counted loop with accumulator

def main():
    n = input("How many numbers do you have? ")
    my_sum = 0.0
    for i in range(n):
        x = input("Enter a number >> ")
        my_sum = my_sum + x
        
    print "\nThe average of the numbers is", my_sum / n

main()
