import numpy as np

# arr1 = np.array([1,2])
# arr2 = np.array([[1,2],[3,4]])

# shape of array

# print(arr1.shape)
# print(arr2.shape)
# print(arr2.dtype)

# a = [1,2,3]
# b = [4,5,6]
# c = [23,56,54,78]

# mathmatical functions
# print(np.sum(a+b))
# print(np.mean(c))  
# print(np.max(c))
# print(np.min(c))
# print(np.sqrt(a))

# elements wise operations
# print(a+b)
# print(a*b)
# print(a**2)

# print(np.zeros((3,2)))
# print(np.ones((2,3)))
# print(np.full((2,1),5))

# print(np.arange(0,10,3)) 
# print(np.random.rand(3,2))

#indexing & slicing 
# a = [43,542, 2342,564,64]
# print(a[1])
# print(a[-1])
# print(a[1:3])

# b =np.array([[1,2,3],
#             [4,5,6]])

# print(b[0,2])
# print(b[1,:])
# print(b[:,2])

#reshape of array

# c = np.array([0,1,2,3,4,5,6,7])
# print(c.reshape(2,4))
# print(c.reshape(4,2))

# print(c.shape)
# print(c.ndim)
# print(c.size)

# print(c > 5)
# print(c[ c > 5])

# a = np.array([1,2,3])

# b = a.copy()
# c = a.view() # shared copy

# a[1] = 100
# print(b)
# print(c)

# marks = np.array([
#     [87,89,45,32,23],
#     [23,46,19,56,78],
#     [97,59,79,55,92],
# ])

# print(np.mean(marks))
# print(np.max(marks))

#mean # max

# student = np.array([
#     [87,89,45,32,23],
#     [23,46,19,56,78],
#     [97,59,79,55,92],
# ])

# print(np.mean(student,axis=1))
# print(np.max(student,axis=0))
# print(np.zeros((5,2)))

# arr = np.arange(1,10).reshape(3,3)
# print(arr)
# print(arr.reshape(3,3))

# arr2 = np.array([34,63,54,56])
# print(np.mean(arr2))
# print(np.max(arr2))
# print(np.min(arr2))
# print(arr2.reshape(2,2))

#Replace all even number in the 

# arr = np.arange([10,60,30,80,25])
# print(arr > 5)
# print(arr[ arr > 5])


# print(arr.reshape(3,4))

arr = np.array([1,2,3,4,5])
arr[arr % 2 == 0] = -1
print(arr)



