import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 100, 100)
y1 = x ** 2.0
y2 = np.log(x)
y3 = np.sin(x)
y4 = np.log10(x)

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('y1=x.^2.0')

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('y2=log(x)')

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('y3=sin(x)')

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('y4=log10(x)')

plt.tight_layout()
plt.show()
