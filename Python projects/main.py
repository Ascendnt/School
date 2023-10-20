print("Enter Marks Obtained in 5 Subjects: ")

rename = int(input("Enter Marks Obtained in 5 Subjects: "))
# math = int(input(90))
# science = int(input(91))
# english = int(input(91))
# filipino = int(input(92))

avg = rename / 4

if avg >= 99:
    print("With Highest Honors")
elif avg >= 97:
    print("With High Honors")
elif avg >= 94:
    print("With Honor")
elif avg >= 89:
    print("Passed")
elif avg <= 74:
    print("Failed")


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
xx, yy = np.meshgrid(x ,y)
z = 2 - (xx ** 2 + yy ** 2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, z)

plt.contour(xx, yy, z)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Surface with Contour Plot')

plt.show()







