import numpy as np
import matplotlib.pyplot as plt

# a. x[n] = 3u[n + 3], −8 ≤ n ≤ 8
n_a = np.arange(-8, 9)
x_a = 3 * (n_a + 3 >= 0)

plt.subplot(3, 2, 1)
plt.stem(n_a, x_a)
plt.title('a. x[n] = 3u[n + 3]')
plt.xlabel('n')
plt.ylabel('x[n]')

# b. x[n] = -2δ[n + 5], −8 ≤ n ≤ 8
n_b = np.arange(-8, 9)
x_b = -2 * (n_b + 5 == 0)

plt.subplot(3, 2, 2)
plt.stem(n_b, x_b)
plt.title('b. x[n] = -2δ[n + 5]')
plt.xlabel('n')
plt.ylabel('x[n]')

# c. x[n] = n(r[n − 2]), −7 ≤ n ≤ 5
n_c = np.arange(-7, 6)
x_c = n_c * (n_c - 2 >= 0)

plt.subplot(3, 2, 3)
plt.stem(n_c, x_c)
plt.title('c. x[n] = n(r[n − 2])')
plt.xlabel('n')
plt.ylabel('x[n]')

# d. x[n] = 3u[n + 3] − δ[n − 5], −3 ≤ n ≤ 5
n_d = np.arange(-3, 6)
x_d = 3 * (n_d + 3 >= 0) - (n_d - 5 == 0)

plt.subplot(3, 2, 4)
plt.stem(n_d, x_d)
plt.title('d. x[n] = 3u[n + 3] − δ[n − 5]')
plt.xlabel('n')
plt.ylabel('x[n]')

# e. x[n] = 3r[n − 2] + 2u[n + 1], −5 ≤ n ≤ 5
n_e = np.arange(-5, 6)
x_e = 3 * (n_e - 2 >= 0) + 2 * (n_e + 1 >= 0)

plt.subplot(3, 2, 5)
plt.stem(n_e, x_e)
plt.title('e. x[n] = 3r[n − 2] + 2u[n + 1]')
plt.xlabel('n')
plt.ylabel('x[n]')

plt.tight_layout()
plt.show()
