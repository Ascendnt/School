import matplotlib.pyplot as plt
import numpy as np

def unitsample(s,n1,n2):
    n=np.arange(n1,n2)
    x=np.zeros_like(n)
    x[n==s]=1
    return n, x
#Given
na, xa = unitsample(0, -12, 16) #original
nb, xb = unitsample(-2, -12, 16) # advance
nc, xc = unitsample(9, -12, 16) # delay

#Plot
plt.subplot(3, 1, 1)
plt.stem(na, xa)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Unit Sample')
plt.grid(True)
plt.xticks(np.arange(-12, 16, 1))

#Delayed Unit Sample
plt.subplot(3, 1, 2)
plt.stem(nb, 2 * xb)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Advanced Unit Sample ')
plt.grid(True)
plt.xticks(np.arange(-12, 16, 1))

#Advanced Unit Sample
plt.subplot(3, 1, 3)
plt.stem(nc, xc)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Delayed Unit Sample')
plt.grid(True)
plt.xticks(np.arange(-12, 16, 1))



plt.tight_layout()
plt.show()
