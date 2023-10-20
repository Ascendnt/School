import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 100 ,100)
y1 = x ** 2.0
y2 = x ** 2.1
y3 = x ** 2.2
y4 = x ** 2.3

plt.plot(x, y1, label='x^2.0', color='b')
plt.plot(x, y2, label='x^2.1', color='g')
plt.plot(x, y3, label='x^2.2', color='r')
plt.plot(x, y4, label='x^2.3', color='m')

plt.grid(True)
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Multiple Graph')
plt.show()
