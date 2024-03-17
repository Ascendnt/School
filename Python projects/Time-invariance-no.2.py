import matplotlib.pyplot as plt
import numpy as np

def sigshift (x,m,n0):
    ns = m+n0;
    xs = x;
    return ns, xs
def sigadd (n1, x1, n2, x2):
    n = np.arange(min(min(n1),min(n2)), max(max(n1), max(n2)) + 1)
    y1 = np.zeros(len(n))
    y2 = np.zeros(len(n))
    index1 = (n >= min(n1)) & (n <= max(n1))
    index2 = (n >= min(n2)) & (n <= max(n2))
    y1[index1] = x1
    y2[index2] = x2
    y = y1 + y2
    return n, y
n = np.arange(-3, 4)
x = np.array([-1, 1, 3, 4, 3, -2, 1])

#Original Input
x1 = x; nx1 = n;

#Shifted input
nx2, x2 = sigshift(x1, nx1, 0)

#Original Output
na, ya = sigshift(x1, nx1, 0)
nb, yb = sigshift(x1, nx1, -1)
ny1, y1 = sigadd(na, ya, nb, yb)

#Shifted Output
na, ya = sigshift(x2, nx2, 0)
nb, yb = sigshift(x2, nx2, -1)
ny2, y2 = sigadd(na, ya, nb, yb)

#Subplot
plt.subplot(2,2,1); plt.stem(nx1, x1);
plt.xlabel('n'); plt.ylabel('x[n]');
plt.title('Input')
plt.grid(True)

plt.subplot(2,2,2); plt.stem(ny1, y1);
plt.xlabel('n'); plt.ylabel('y[n]');
plt.title('Output')
plt.grid(True)

plt.subplot(2,2,3); plt.stem(nx2, x2);
plt.xlabel('n'); plt.ylabel('x[n]');
plt.title('Shifted Input')
plt.grid(True)

plt.subplot(2,2,4); plt.stem(ny2, y2);
plt.xlabel('n'); plt.ylabel('y[n]');
plt.title('Shifted Output')
plt.grid(True)

plt.tight_layout()
plt.show()
