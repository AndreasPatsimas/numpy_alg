import numpy as np

arr= np.array([[1, 2], [3, 4],[5,6]])
np.reshape(arr, (1, 6))
# print(arr)

arr.reshape(6)
# print(arr)

arr= np.array([[1, 2], [3, 4],[5,6]])

FL=arr.flatten()
RL=arr.ravel()

FL[2]=9999
RL[2]=8888

print(FL)
print(RL)