import numpy as np

a = np.arange(1,13).reshape(3,4)
print(a)

def lightCopy():
    sub = a[:2, :2]
    sub[0][0] = 100
    print(sub)
    print(a)

def deepCopy():
    sub = np.copy(a[:2, :2])
    sub[0][0] = 100
    print(sub)
    print(a)

# lightCopy()
deepCopy()