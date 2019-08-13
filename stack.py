import numpy as np
import random

a = np.random.randint(1,10,size=(2,3),dtype=int)
b = np.random.randint(1,10,size=(2,3),dtype=int)
print(a)
print(b)

hstack = np.hstack((a,b))
vstack = np.vstack([a,b])   

print("hstack: ", hstack)
print("vstack: ", vstack)