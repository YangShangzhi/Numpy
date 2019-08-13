import numpy as np

b = np.arange(1,5)
# print(b[2])

x = np.arange(1,13)
a = x.reshape(4,3)
print("Array: \n", a)


# [row, column] --> [start:stop:step , start:stop:step]
# Slice get each row, second column
print("second column: \n", a[: , 1])

#Slice get each row, first and second column
print("first and column: \n", a[: , 0:2])