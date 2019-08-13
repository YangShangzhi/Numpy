import numpy as np

a = np.arange(1,13)
b = np.random.randint(1,10,size=(2,4),dtype=int)
c = np.random.randint(1,10,size=(2,4),dtype=int)
print(b)
print(c)

# split average
res = np.split(a,4,axis=0)
# print(res)

# split by array 
res2 = np.split(a,[3,5])
# print(res2)

# split by np.hsplit()
row,col = np.hsplit(b,2)
print(row)
print(col)

# split by np.vsplit()
row2,col2 = np.vsplit(c,2)
print(row2)
print(col2)