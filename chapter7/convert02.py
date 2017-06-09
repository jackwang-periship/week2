'''
Created on Jun 7, 2017

@author: jwang02
'''
def main():
    celsius = input("What is the Celsius temperature? ")
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print "The temperature is", fahrenheit, "degrees fahrenheit."
    
    if fahrenheit > 90:
        print "It's really hot out there, be careful!"
    if fahrenheit < 30:
        print "Brrrr. Be sure to dress warmly!"
    
main()
    
