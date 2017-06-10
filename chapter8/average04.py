'''
Created on Jun 9, 2017

@author: student
'''
#    A program to average a set of numbers
#    Illustrates sentinel loop using empty string as sentinel

def main():
    my_sum = 0.0
    count = 0
    xStr = raw_input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        my_sum = my_sum + x
        count = count + 1
        xStr = raw_input("Enter a number (<Enter> to quit) >> ")
    print "\nThe average of the numbers is", my_sum / count

main()
