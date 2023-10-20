import matplotlib.pyplot as plt
import numpy as np

def unitramp(s, n1, n2):
    n = np.arange(n1, n2)
    x = np.maximum(0, n-s)
    return n, x

#Given
na, xa = unitramp(0, -9, 8) #Original
nb, xb = unitramp(3, -9, 8) #Delay
nc, xc = unitramp(-4, -9, 8) #Advance

#Plot
plt.subplot(3, 1, 1)
plt.stem(na, xa, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-9, 8, 1))
plt.title('Unit Ramp')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(nb,2 * xb, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-9, 8, 1))
plt.title('Delayed Unit Ramp by 3 sample')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(nc, xc, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-9, 8, 1))
plt.title('Advanced Unit Ramp by 3 sample')
plt.grid(True)

plt.tight_layout()
plt.show()