'''
Created on Jun 7, 2017

@author: jwang02
'''
'''A function returning a string and using a local variable'''

def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result

print(lastFirst('Benjamin', 'Franklin'))
print(lastFirst('Andrew', 'Harrington'))
