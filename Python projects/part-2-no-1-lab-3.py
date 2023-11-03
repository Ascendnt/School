#x[-n + 3] * y[-n-4] * z[-n + 2]
import matplotlib.pyplot as plt
import numpy as np

def sigshift(x,m,n0): #m interval, n0 shift
    ns = m + n0
    xs = x
    return ns, xs

def flipsig(n,x):
    xf = x[::-1] #flipped x
    nf = -n[::-1] #flipped n
    return nf, xf

def sigmult(n1, x1, n2, x2, n3, x3):
    n = np.arange(min(min(n1), min(n2), min(n3)), max(max(n1), max(n2), max(n3))+ 1)
    y1 = np.zeros(len(n))
    y2 = np.zeros(len(n))
    y3 = np.zeros(len(n))
    index1 = (n >= min(n1)) & (n <= max(n1))
    index2 = (n >= min(n2)) & (n <= max(n2))
    index3 = (n >= min(n3)) & (n <= max(n3))
    y1[index1] = x1
    y2[index2] = x2
    y3[index3] = x3
    y = y1 * y2 * y3
    return n, y

#Given
x1 = np.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
n1 = np.arange(-4, 5)
x2 = np.array([2, 4, 6, 8, 10, -1, -3, -5, -7, -9])
n2 = np.arange(-1, 9)
x3 = np.array([1, 2, 4, 6, 5, 6, 2, -1, -3, -2])
n3 = np.arange(-6, 4)

# 2x[n]
na = n1
xa = 2 * x1

# 3y[-n]
nb, xb = flipsig(n2, 3 * x2)
nb, xb = sigshift(x2, n2, -4)

#z[n+2]
nc, xc = sigshift(x3, n3, -2)

#Signal operation
nd, xd = sigmult(na, xa, nb, xb, nc, xc)

#Plot 2x[n]
plt.subplot(2, 2, 1); plt.stem(na, xa)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('2x[n]'); plt.grid(True)

#Plot 3y[-n]
plt.subplot(2, 2, 2); plt.stem(nb, xb)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('3y[-n]'); plt.grid(True)

#Plot z[n+2]
plt.subplot(2, 2 , 3); plt.stem(nc, xc)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('z[n+2]'); plt.grid(True)

#Plot Signal Operation
plt.subplot(2, 2, 4); plt.stem(nd, xd)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('Output Signal'); plt.grid(True)

plt.tight_layout()
plt.show()




    
