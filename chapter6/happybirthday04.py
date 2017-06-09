'''
Created on Jun 7, 2017

@author: jwang02
'''
def happy():
    print "Happy birthday to you!"
    

def signFred():
    happy()
    happy()
    print "Happy birthday, dear Fred."
    happy()


def signLucy():
    happy()
    happy()
    print "Happy birthday, dear Lucy."
    happy()

def sing(person):
    happy()
    happy()
    print "Happy birthday, dear", person + "."
    happy()
    
    
    
def main():
    sing("Fred")
    print
    sing("Lucy")
    print
    sing("Elmer")

    
main()    

    
    