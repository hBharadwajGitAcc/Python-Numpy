# Task 1
import numpy as np
np.zeros((5,5))


# Task 2
import numpy as np
np.arange(10,105,5)


# Task 3
a = np.array([[10,20,30,40,50,60]])
a.shape = (2,3)
print(a.size)
len(a)
type(a.dtype)
a.dtype


# Task 4
a = np.array([1,2,3])
b = np.array([4,5,6])
np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)


# Task 5
arr = np.arange(10,91,10)
arr.shape = (3,3)
arr
arr[:,2]
arr[1,:]
##arr[0][:2]
##arr[:2,0]
arr[0][0]
##arr[:,1][1]

