import matplotlib.pyplot as plt
import numpy as np

n = np.arange (-4, 4)
x = np.array ([3, -2, 5, 0 ,1, 2, -2, 3])

# Stem
plt.subplot (2, 1, 1)
plt.stem (n, x)
plt.xlabel ('n')
plt.ylabel ('x[n]')
plt.title ('Stem Sequence')
plt.grid(True)

# Plot
plt.subplot(2, 1, 2)
plt.plot(n, x, marker='o', linestyle='-',markersize=5)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Plot Sequence')
plt.grid(True)

plt.tight_layout()
plt.show()


