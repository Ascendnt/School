import matplotlib.pyplot as plt
import numpy as np

def sigshift (x,m,n0): #m sequencecount, n0 shift
    ns = m+n0
    xs = x
    return ns,xs

def flipsig (n,x):
    xf = x[::-1];  #flipped x
    nf = -n [::-1];  #flipped n
    return nf, xf

def downsample(x,n1,n2,f):
    factor = f
    nd = np.arange(n1/f, n2/f)
    xd = x[::f]
    return nd,xd


#Given
xa = np.array([4,-3,2,-1,2,-7,2]); #x[n]
na = np.arange (-4,3)

#x[2n-2]
nb, xb = downsample(xa,-4,3,2);#x[2n]
nb ,xb = sigshift(xb,nb,2)#x[2n-2]

#x[n]
nc, xc = flipsig (na,xa)

# x[-n+2]
nd,xd = sigshift(xc,nc,2); 

#x[n]
plt.subplot(2,2,1); plt.stem(na,xa)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('x[n]'); plt.grid(True)

#x[2n-2]
plt.subplot(2,2,2); plt.stem(nb,xb)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('x[2n-2]'); plt.grid(True)

#x[-n]
plt.subplot(2,2,3); plt.stem(nc,xc)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('x[-n]'); plt.grid(True)

#x[-n+2]
plt.subplot(2,2,4); plt.stem(nd,xd)
plt.xlabel('n'); plt.ylabel('x[n]')
plt.title('x[-n+2]'); plt.grid(True)

plt.tight_layout()
plt.show()


