from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
#y = x.copy().T # transpose
#z = np.cos(x ** 2 + y ** 2)

pi = np.pi
imax = 101
jmax = 101
dx = 1.0/(imax-1)
dy = 1.0/(jmax-1)
x = np.ndarray((imax, jmax))
y = np.ndarray((imax, jmax))

for i in range(imax):
    for j in range(jmax):
        x[i][j] = i*dx
        y[i][j] = j*dy


z = np.sin(pi * x) * np.sin( pi * y)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()
