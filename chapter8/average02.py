'''
Created on Jun 9, 2017

@author: student
'''
#    A program to average a set of numbers
#    Illustrates interactive loop with two accumulators

def main():
    my_sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = input("Enter a number >> ")
        my_sum = my_sum + x
        count = count + 1
        moredata = raw_input("Do you have more numbers (yes or no)? ")
    print "\nThe average of the numbers is", my_sum / count

main()
