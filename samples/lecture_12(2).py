import numpy as np

a1 = np.array([[6,-9,1],[4,24,8]])
result_1 = np.dot(a1,2)
print(result_1)

a2 = np.array([[1,0],[0,1]])
a3 = np.array([[6,-9,1],[4,24,8]])
result_2 = np.dot(a2,a3)
print(result_2)

a4 = np.array([[4,3],[3,2]])
a5 = np.array([[-2,3],[3,-4]])
result_3 = np.dot(a4,a5)
print(result_3)