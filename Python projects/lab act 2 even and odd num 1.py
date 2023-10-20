import numpy as np
import matplotlib.pyplot as plt

def unitstep (s, n1, n2):
    n = np.arange(n1, n2)
    x = np.zeros_like(n)
    x [n >= s] = 1
    return n, x

def unitramp(s, n1, n2):
     n = np.arange(n1, n2)
     x = np.maximum(0, n-s)
     return n, x

def flipsig(n, x):
    x = x[:: -1] #flipped x
    n = -n[::-1] #flipped n
    return n, x

def sigadd(n1, x1, n2, x2):
    n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2)) + 1)
    y1 = np.zeros(len(n))
    y2 = np.zeros(len(n))
    index1 = (n >= min(n1)) & (n <= max(n1))
    index2 = (n >= min(n2)) & (n <= max(n2))
    y1[index1] = x1
    y2[index2] = x2
    y = y1 + y2
    return n, y

#Given
na, xa = unitstep(0, -7, 8)
nb, xb = unitramp(-2, -7, 8)
nc, xc = sigadd(na, xa, nb, 2 * xb)
nf, xf = flipsig(nc, xc)
ne, xe = sigadd(nc, 0.5 * xc, nf, 0.5 * xf)
no, xo = sigadd(nc, 0.5 * xc, nf, -0.5 * xf)

#Original Sequence
plt.subplot(2, 2, 1) ; plt.stem(nc, xc, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-7, 8, 1))
plt.yticks(np.arange(0, 25, 5))
plt.title('Original Sequence')
plt.grid(True)

#Flipped Sequence
plt.subplot(2, 2, 2) ; plt.stem(nf, xf, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-7, 8, 1))
plt.yticks(np.arange(0, 25, 5))
plt.title('Flipped Sequence')
plt.grid(True)

#Even Part
plt.subplot(2, 2, 3) ; plt.stem(ne, xe, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-7, 8, 1))
plt.yticks(np.arange(0, 11, 5))
plt.title('Even Part')
plt.grid(True)

#Odd Part
plt.subplot(2, 2, 4) ; plt.stem(ne, xe, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(np.arange(-7, 8, 1))
plt.yticks(np.arange(-10, 11, 5))
plt.title('Odd Part')
plt.grid(True)

plt.tight_layout()
plt.show()

