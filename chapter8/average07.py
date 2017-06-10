'''
Created on Jun 9, 2017

@author: student
'''
#     Computes the average of numbers listed in a file.
#     Works with multiple numbers on a line.

import string

def main():
    fileName = raw_input("What file are the numbers in? ")
    infile = open(fileName,'r')
    my_sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        # update sum and count for values in line
        for xStr in string.split(line, ","):
            my_sum = my_sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print "\nThe average of the numbers is", my_sum / count

main()

