'''
Created on Jun 7, 2017

@author: jwang02
'''
import math

def main():
    print "This program finds the real solutions to a quadratic"
    print
    
    a, b, c = input("Please enter the coefficients (a, b, c): ")
    
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    
    print
    print "The solutions are: ", root1, root2
    
main()

'''
The way to solve "ax2 + bx + c = 0" for the value of x is to factor 
the quadratic, set each factor equal to zero, and then solve each factor. 
But sometimes the quadratic is too messy, 
or it doesn't factor at all, or you just don't feel like factoring. 
While factoring may not always be successful, 
the Quadratic Formula can always find the solution.

The Quadratic Formula uses the "a", "b", and "c" 
from "ax2 + bx + c", where "a", "b", and "c" are just numbers; 
they are the "numerical coefficients" of the quadratic equation they've given you to solve.



'''