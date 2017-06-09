'''
Created on Jun 7, 2017

@author: jwang02
'''
'''program causing an error with an undefined variable'''

def main():
    x = 3
    f()

def f():
    print(x)  # error: f does not know about the x defined in main

main()

'''A change to badScope.py avoiding any error by passing a parameter'''
'''
def main():
    x = 3
    f(x)

def f(y):
    print(y)  

main()
'''