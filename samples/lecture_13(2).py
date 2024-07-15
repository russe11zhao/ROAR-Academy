import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.0, 3.5, 0.5)
y = np.array([2., 3.,4.,2.5,1])
plt.plot(x, y, 'b', 1)
plt.xlim(1.0,3.0)
plt.ylim(1.0,4.0)
plt.xticks(np.arange(1.0,3.5,0.5), np.arange(1.0,3.5, 0.5))
plt.title('Sample graph!')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
print(x)