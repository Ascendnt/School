import numpy as np
import matplotlib.pyplot as plt

def unitstep (s, n1, n2):
    n = np.arange(n1, n2)
    x = np.zeros_like(n)
    x [n >= s] = 1
    return n, x

def unitsample(s, n1, n2):
    n = np.arange(n1, n2)
    x = np.zeros_like(n)
    x [n == s] = 1
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
na, xa = unitsample(-5, -8, 9)
nb, xb = unitstep(-3, -8, 9)
nc, xc = unitramp(2, -8, 9)
nd, xd = sigadd(na, 3 * xa, nb, xb)
nd, xd = sigadd(nd, xd, nc, -xc) # total sigadd
nf, xf = flipsig(nd, xd) # flipped signal
ne, xe = sigadd(nc, 0.5 * xd, nf, 0.5 * xf) # even part
no, xo = sigadd(nc, 0.5 * xd, nf, -0.5 * xf) # odd part

#Original Sequence
plt.subplot(2, 2, 1) ; plt.stem(nd, xd, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Original Sequence')
plt.grid(True)

#Flipped Sequence
plt.subplot(2, 2, 2) ; plt.stem(nf, xf, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Flipped Sequence')
plt.grid(True)

#Even Part
plt.subplot(2, 2, 3) ; plt.stem(ne, xe, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Even Part')
plt.grid(True)

#Odd Part
plt.subplot(2, 2, 4) ; plt.stem(no, xo, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Odd Part')
plt.grid(True)

plt.tight_layout()
plt.show()

