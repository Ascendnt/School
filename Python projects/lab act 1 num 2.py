import numpy as np
import matplotlib.pyplot as plt

x = np.linspace (-10, 10, 21)
y = 2*x +3

plt.stem(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Stem Plot")
plt.grid(True)
plt.xticks(np.arange(-10, 11, 1))
plt.yticks(np.arange(-25, 26, 5))
plt.show()
