import matplotlib.pyplot as plt
import numpy as np

def sigshift(x, m, n0):
    ns = m + n0
    xs = x
    return ns, xs

def flipsig(n, x):
    xf = x[::-1]  # flipped x
    nf = -n[::-1]  # flipped n
    return nf, xf

# def downsample(x, n1, n2, f):
#     factor = f
#     nd = np.arange(n1 / f, n2 / f)
#     xd = x[::f]
#     return nd, xd

def upsample(x, n1, n2, f):
    factor = f
    nu = np.arange(n1, n2, 1 / factor)
    nu = nu * f
    xu = np.zeros(len(nu))

    for i, item in enumerate(x):
        xu[i * f] = item

    return nu, xu

# Given
xa = np.array([5, -1, 4, -7, 8, 2, 1, 0, -2])  # x[n]
na = np.arange(-2, 7)

# Upsample x[-n-2/2]
nb, xb = upsample(xa, -2, 7, 2)
nb, xb = flipsig(nb, xb)
nb, xb = sigshift(xb, nb, -2)

# Flip and shift x[n] to create x[-n-1]
nc, xc = flipsig(xa, na)  # Flip the original signal
nc, xc = sigshift(nc, xc, -1)

# Calculate 3x[n-2]
nd, xd = sigshift(xa, na, 2)

# x[n]
plt.subplot(2, 2, 1)
plt.stem(na, xa)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n]')
plt.grid(True)

# x[-n-2/2]
plt.subplot(2, 2, 2)
plt.stem(nb, xb)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[-n-2/2]')
plt.grid(True)


# x[-n-1]
plt.subplot(2, 2, 3)
plt.stem(nc, xc)
plt.xlabel('n')
plt.ylabel('x[-n-1]')
plt.title('x[-n-1]')
plt.grid(True)

# 3x[n-2]
plt.subplot(2, 2, 4)
plt.stem(nd, 3 * xd)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('3x[n-2]')
plt.grid(True)

plt.tight_layout()
plt.show()
