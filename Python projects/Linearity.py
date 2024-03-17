import matplotlib.pyplot as plt
import numpy as np

def sigshift(x,m,n0): #m interval, n0 shift
    ns = m+n0;
    xs = x;
    return ns, xs
	
def sigadd(n1, x1, n2, x2):
    n=np.arange(min(min(n1),min(n2)), max (max(n1), max(n2)) + 1)
    y1 = np.zeros(len(n))
    y2 = np.zeros(len(n))
    index1 = (n >= min(n1)) & (n <= max(n1))
    index2 = (n >= min(n2)) & (n <= max(n2))
    y1[index1] = x1
    y2[index2] = x2
    y = y1 + y2
    return n, y
 

n = np.arange(-3, 4)
x= np.array([-1, 1, 3, 4, 3, -2, 1])

#Original Input kx[n]
x1 = x; nx1 = n;

#Input Response kx[n]
x2 = 2*x; nx2 = n;

#Original Output y[n]
ya = x1 ; na=n;
na, ya = sigshift(x1, nx1, 0)
nb, yb = sigshift(x1, nx1, -1)
ny1,y1 = sigadd(na, ya, na, ya)
ny1,y1 = sigadd(ny1,y1,na, -ya)
#Output Response ky[n]
ya = x2; na=n;
na, ya = sigshift(x2,nx2,0)
nb, yb = sigshift(x2,nx2,-1)
ny2, y2 = sigadd(na, ya, nb, yb)
ny2, y2 = sigadd(ny2, y2, nb, -yb)


#Combination
nx3, x3 = sigadd(nx1, x1, nx2, x2)
ny3, y3 = sigadd(ny1, y1, ny2, y2)


#Subplot
plt.subplot(3,2,1); plt.stem(nx1, x1);
plt.xlabel('n'); plt. ylabel('x[n]');
plt.title('Input x1 = x')
plt.grid(True)

plt.subplot(3,2,2); plt.stem(ny1, y1);
plt.xlabel('n'); plt. ylabel('x[n]');
plt.title('Output y1')
plt.grid(True)

plt.subplot(3,2,3); plt.stem(nx2, x2);
plt.xlabel('n'); plt. ylabel('x[n]');
plt.title('Input x2 = 2x')
plt.grid(True)

plt.subplot(3,2,4); plt.stem(nx3, x3);
plt.xlabel('n'); plt. ylabel('x[n]');
plt.title('Output y2')
plt.grid(True)

plt.subplot(3,2,5); plt.stem(nx3, x3);
plt.xlabel('n'); plt. ylabel('x[n]');
plt.title('Combination of Input Responces')
plt.grid(True)

plt.subplot(3,2,6); plt.stem(ny3, y3);
plt.xlabel('n'); plt. ylabel('x[n]');
plt.title('Combination of Output Responces')
plt.grid(True)

plt.tight_layout()
plt.show()
