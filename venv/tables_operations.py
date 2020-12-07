import numpy as np
import matplotlib.pyplot as plt

arr1 = np.random.rand(3,3)
print(arr1)

x = np.linalg.det(arr1)
print(x)

arr2 = np.linalg.inv(arr1)
print(arr2)

# Θεωρήστε τον πολλαπλασιαμό τριών πινάκων arr3=arr2· arr1· arr2-1
# Υλοποιήστε τον πολλαπλασιασμό με χρήση της συνάρτησης και της μεθόδου dot
arr1 = np.random.rand(3,3)
arr2 = np.random.rand(3,3)
arr3 = np.dot(arr2, np.dot(arr1, np.linalg.inv(arr2)))
arr3 = arr2.dot(arr1.dot(np.linalg.inv(arr2)))

####################################################################################################################

x = np.array([[0, 1, 2, 3], [1,1,1,1]])
y = np.array([-1, 0.2, 0.9, 2.1])
a, b = np.linalg.lstsq(x.transpose(), y.transpose(), rcond=None)[0]
plt.plot(x[0], y, 'go', label='Original data', markersize=10)
plt.plot(x[0], a*x[0] + b, 'r-.', label='Fitted line')
plt.ylabel('Time')
plt.xlabel('Distance')
plt.title('T vs D')
plt.legend(['Original', 'Least Squares'])
plt.grid(color='k', linestyle=':', linewidth=2)
plt.show()

####################################################################################################################