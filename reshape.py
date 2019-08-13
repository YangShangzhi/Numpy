import numpy as np

a = np.arange(1,25,dtype = int)
print(a)

# object.reshape()
b = a.reshape(3,8)
print(b)

# numpy.reshape()
c = np.reshape(a, (4,6))
print(c)

# reshape to 1 dimension array
arr1 = b.reshape(-1)
arr2 = b.ravel()
arr3 = b.flatten()
print(arr1)
print(arr2)
print(arr3)
