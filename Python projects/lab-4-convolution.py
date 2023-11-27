import matplotlib.pyplot as plt
import numpy as np


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




# Given

nx = np.arange(-2, 3)
x = np.array([2, 4, 8, 10, 12])

nh = np.arange(-1, 4)
h = np.array([1, 0, 0, 0, 1])

# Input Signal
plt.subplot(3, 1, 1)
n = np.arange(min(nx), min(nx) + len(x))
x = x
plt.stem(n, x)
plt.title("Input Signal")
plt.xlabel('n')
plt.ylabel('x[n]')


# Impulse
plt.subplot(3, 1, 2)
n = np.arange(min(nh), min(nh) + len(h))
h = h
plt.stem(n, h)
plt.title('Impulse Response')
plt.xlabel('n')
plt.ylabel('x[n]')

# Convolution
plt.subplot(3, 1, 3)
y = np.convolve(x, h, mode='full')
n = np.arange(min(nx) + min(nh), min(nx) + min(nh) + len(y))
plt.stem(n, y)
plt.title('Convolution Output')
plt.xlabel('n')
plt.ylabel('x[n]')

plt.tight_layout()
plt.show()
