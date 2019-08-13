import numpy as np


def randomTest():

    #random num from 0-1, 1 dimension
    a = np.random.random(size=5)
    print(a)
    print(type(a))

    # random num from 0-1, 2 dimension
    b = np.random.random(size=(3,4))
    print(b)

def randomintTest():

    # random integer from 1-5, 1 dimension
    a = np.random.randint(6, size=10)
    print(a)
    print(type(a))
    print("default dtype: ", a.dtype)

    # random integer from 5-10, 2 dimension
    b = np.random.randint(5,11,size=(4,3))
    print(b)

# 期望为0，方差是1的标准正态分布
def randnTest():
    a = np.random.randn(4)
    print(a)
    print(type(a))

# 指定期望和方差的正态分布
def normalTest():
    a = np.random.normal(loc=2, scale=3, size=5)
    print(a)
    print(type(a))


# randomTest()
# randomintTest()
# randnTest()
normalTest()