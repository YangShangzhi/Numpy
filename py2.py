import numpy as np

def testZeros():
    a = np.zeros(5, dtype = int)
    print(a)

def testOnes():
    b = np.ones((2,5), dtype = int)
    print(b)

def testEmptys():
    c = np.empty(5, dtype = float)
    print(c)

def testLinespace():
    d = np.linspace(2,10,num=5,endpoint=True,dtype=int)
    print(d)

def testLogspace():
    e = np.logspace(0,9,10,base=2)
    print(e)


# testZeros()
# testOnes()
# testEmptys()
# testLinespace()
testLogspace()