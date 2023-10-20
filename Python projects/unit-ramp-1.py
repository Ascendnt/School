import matplotlib.pyplot as plt
import numpy as np

def unitramp(s, n1, n2):
    n = np.arange(n1, n2)
    x = np.maximum(0, n-s)
    return n, x

#Given
na, xa = unitramp(0, -8, 11) #Original
nb, xb = unitramp(3, -8, 11) #Delay
nc, xc = unitramp(-3, -8, 11) #Advance

#Plot
plt.subplot(3, 1, 1)
plt.stem(na, xa, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-8, 11, 1))
plt.title('Unit Ramp')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(nb, xb, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-8, 11, 1))
plt.title('Delayed Unit Ramp by 3 sample')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(nc, 2 * xc, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-8, 11, 1))
plt.title('Advanced Unit Ramp by 3 sample')
plt.grid(True)

plt.tight_layout()
plt.show()