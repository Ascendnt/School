##import numpy as np 
##import matplotlib.pyplot as plt
##
##n = range(-8, 8, 1)
##y = []
##for i in range(len(n)):
##    temp = (1 if n[i]>=0 else 0)
##    y.append(3 * temp)
##    
##print(n)
##print(y)
##
###plotting the graph
##plt.grid(True)
##plt.stem(n, y)
##plt.axis([-1, 8, -1, 8])
##plt.show()


## number 1 integ 3

import numpy as np 
import matplotlib.pyplot as plt

n = range(-11, 9, 1) ## delayed or advanced
y = []
for i in range(len(n)):
    impulse = (1 if n[i]>=0 else 0)
    y.append(impulse) # changeable
    
print(n)
print(y)

#plotting the graph
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.stem(n, y)
plt.axis([-8.1, 8.1, -0.1, 8.2])
plt.show()
