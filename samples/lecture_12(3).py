import numpy as np

row_0 = [0,1,2,3,4,5]
row_1 = [10,11,12,13,14,15]
row_2 = [20,21,22,23,24,25]
row_3 = [30,31,32,33,34,35]
row_4 = [40,41,42,43,44,45]
row_5 = [50,51,52,53,54,55]
arr = np.array([row_0,row_1,row_2,row_3,row_4,row_5])

pink = arr[1,2:4]
green = arr[2:4,4:]
blue = arr[:,1]
orange = arr[2::2,::2]
print(pink)
print(green)
print(blue)
print(orange)