import matplotlib.pyplot as plt
import numpy as np

def sigshift(x, m, n0): #m sequencecount, n0 shift
    ns = m + n0;
    xs = x;
    return ns, xs

def flipsig(n, x):
    xf = x[:: -1] # flipped x
    nf = -n[:: -1] # flipped n
    return nf, xf

def upsample(x, n1, n2, f):
    factor = f;
    nu = np.arange(n1, n2, 1/factor);
    nu = nu * f;
    xu = np.zeros(len(nu));

    for i, item in enumerate(x):
        xu[i * f] = item;

    return nu, xu

def downsample(x, n1, n2, f):
    factor = f;
    nd = np.arange(n1/f, n2/f);
    xd = x[:: f];
    return nd, xd

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
x1 = np.array([2, 4, 6, -8, 10, 9, -8, 7]);
n1 = np.arange(-3, 5);

#2x[(-n + 5) / 2]
na, xa = upsample(x1, -3, 5, 2);
na, xa = flipsig(na, xa);
na, xa = sigshift(2 * xa, na, 5);

#-3x[3n - 1]
nb, xb = downsample(x1, -3, 5, 3);
nb, xb = sigshift(3 * xb, nb, 1);

#Signal operation
nc, xc = sigadd(na, xa, nb, -xb);


plt.subplot(2, 2, 1)
plt.stem(n1, x1)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('2x[n]')
plt.grid(True)


plt.subplot(2, 2, 2)
plt.stem(na, xa)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('2x[-n+5/2]')
plt.grid(True)


plt.subplot(2, 2, 3)
plt.stem(nb, xb)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('-3x[3n-1]')
plt.grid(True)


plt.subplot(2, 2, 4)
plt.stem(nc, xc)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Output Signal')
plt.grid(True)

plt.tight_layout();
plt.show();

    
