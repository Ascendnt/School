import numpy as np
import matplotlib.pyplot as plt

a = b = np.linspace(-8, 8, 41)
xx, yy = np. meshgrid(a, b)
c = np.sqrt(xx ** 2 + yy ** 2) + np.finfo(float).eps
d = np.sin(c) / c

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, d)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Surface Plot')

plt.show()
