import matplotlib.pyplot as plt
import numpy as np

def unitstep(s, n1, n2):
    n=np.arange(n1, n2)
    x=np.zeros_like(n)
    x[n>=s] =1
    return n, x

#Given
na, xa = unitstep(0, -10, 9) #original
nb, xb = unitstep(3, -10, 9) #delay
nc, xc = unitstep(-5, -10, 9) #advanced

#Plot
plt.subplot(1, 3, 1); plt.stem(na, xa)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('Unit Step'); plt.grid(True)
plt.xticks(np.arange(-7, 8, 1))

plt.subplot(1, 3, 3); plt.stem(nc, 2.*xc)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('Advanced Unit Step by 5'); plt.grid(True)
plt.xticks(np.arange(-7, 8, 1))

plt.subplot(1, 3, 2); plt.stem(nb, xb)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('Delayed Unit Step by 3'); plt.grid(True)
plt.xticks(np.arange(-7, 8, 1))



plt.tight_layout()
plt.show()
