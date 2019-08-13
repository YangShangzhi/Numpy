import numpy as np

a = np.arange(1,13).reshape(6,2)
print(a)

b = a.transpose()
print(b, b.shape)

c = a.T
print(c, c.shape)

d = np.transpose(a)
print(d, d.shape)