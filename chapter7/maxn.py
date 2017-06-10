'''
Created on Jun 9, 2017

@author: student
'''
#    Finds the maximum of a series of numbers

def main():
    a, b, c = input("Please enter the coefficients (a, b, c): ")
    
    if a >= b:
        if a >= c:
            my_max = a
        else:
            my_max = c
    else:
        if b >= c:
            my_max = b
        else:
            my_max = c

    print "The largest value is", my_max

main()
