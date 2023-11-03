import matplotlib.pyplot as plt
import numpy as np

def unitstep(s, n1, n2):
    n=np.arange(n1, n2)
    x=np.zeros_like(n)
    x[n>=s] =1
    return n, x

def sigshift(x, m, n0):
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

def sigsub(n1, x1, n2, x2):
    n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2)) + 1)
    y1 = np.zeros(len(n))
    y2 = np.zeros(len(n))
    index1 = (n >= min(n1)) & (n <= max(n1))
    index2 = (n >= min(n2)) & (n <= max(n2))
    y1[index1] = x1
    y2[index2] = x2
    y = y1 - y2
    return n, y

#Given
x1 = np.array([2, 4, 6, -8, 10, 9, -8, 7]);
n1 = np.arange(-3, 5);

#2x[-n + 3]
na, xa = upsample(x1, -3, 5, 1);
na, xa = flipsig(n1, x1);
na, xa = sigshift(2 * xa, na, 3)

#3u[n+1] -8 >= n >= 8
nb, xb = unitstep(1, -8, 9) 

#-x[n]
nc, xc = flipsig(n1, x1);
nc, xc = sigshift(xc, nc, 1)

#x[-3n+2]
nd, xd = downsample(x1, -3, 5, 3);
nd, xd = flipsig(n1, x1);
nd, xd = sigshift(xd, nd, 2)

# Signal Operation
ne, xe =  sigadd(na, xa, nb, xb);
ne, xe = sigsub(nc, xc, nd, xd)

#x[n]
plt.subplot(2, 3, 1)
plt.stem(n1, x1)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n]')
plt.grid(True)

#2x[-n + 3]
plt.subplot(2, 3, 2)
plt.stem(na, xa)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('2x[-n + 3]')
plt.grid(True)

#3u[n+1] -8 >= n >= 8
plt.subplot(2, 3, 3)
plt.stem(nb, 3. * xb)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('3u[n+1] -8 >= n >= 8')
plt.grid(True)

#-x[n]
plt.subplot(2, 3, 4)
plt.stem(nc, xc)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('-x[n]')
plt.grid(True)

#x[-3n+2]
plt.subplot(2, 3, 5)
plt.stem(nd, xd)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[-3n+2]')
plt.grid(True)

#Signal Operation
plt.subplot(2, 3, 6)
plt.stem(ne, xe)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Output Signal')
plt.grid(True)

plt.tight_layout();
plt.show();

    
