'''
Created on Jun 7, 2017

@author: jwang02
'''
from __builtin__ import input

def main():
    celsius = input("What is the Celsius temperature? ")
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print "The temperature is", fahrenheit, "degrees fahrenheit."
    
main()