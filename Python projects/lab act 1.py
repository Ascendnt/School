import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100)
y = x**2

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Plot')
plt.grid(True)
plt.xticks(np.arange(0,101,10))
plt.show()
