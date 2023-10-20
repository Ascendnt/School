import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0, 2*np.pi, 0.02)
a1 = 0.7 * theta
a2 = 5 * np.cos(theta)
a3 = 3* (1 - np.cos(theta))
a4 = 6 * np.sin(4 * theta)
r = np.array([a1, a2, a3, a4])

PolarGraph = plt.polar(theta, r.T, "*")
plt.setp(PolarGraph, linewidth = 2)
plt.legend(["spiral", "circle", "heart", "rose"])
plt.show()
