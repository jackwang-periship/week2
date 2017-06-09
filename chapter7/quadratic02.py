'''
Created on Jun 8, 2017

@author: jwang02
'''
import math

def main():
    print "This program finds the real solutions to a quadratic"
    print
    
    a, b, c = input("Please enter the coefficients (a, b, c): ")
    
    
    discrim = b * b - 4 * a * c
    if discrim >= 0:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        
        print
        print "The solutions are: ", root1, root2
#     else:
#         print "Negative numbers do not have real roots."
    
main()


'''
1,2,1

'''