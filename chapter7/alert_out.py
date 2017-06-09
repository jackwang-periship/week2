'''
Created on Jun 8, 2017

@author: jwang02
'''
from sys import argv

def ALERTprint(msg):
    print "\nERROR: ", msg
    
if __name__ == '__main__':
    scriptNAME, parm1, parm2 = argv
    ALERTprint(parm1)
    ALERTprint(parm2)
