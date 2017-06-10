'''
Created on Jun 9, 2017

@author: student
'''
#     Computes the average of numbers listed in a file.

def main():
    fileName = raw_input("What file are the numbers in? ")
    infile = open(fileName,'r')
    my_sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        my_sum = my_sum + eval(line)
        count = count + 1
        line = infile.readline()
    print "\nThe average of the numbers is", my_sum / count

main()

