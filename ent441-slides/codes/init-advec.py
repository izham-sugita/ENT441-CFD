import numpy as np
import matplotlib.pyplot as plt

N = 1001
#array for initial condition and final solution
u = np.ndarray((N,), dtype=np.float32)
un = np.ndarray((N,), dtype=np.float32)
xg = np.ndarray((N,), dtype=np.float32)

L = 10.0
dx = L / (N-1)

#initial condition
for i in range(N):
    xg[i] = i*dx
    u[i] = 0.0
    un[i] = 0.0
    if xg[i] >=0.2*L and xg[i] <=0.4*L:
        u[i] = 1.0
        un[i] = 1.0

filename = "init.png"
display = "t = 0.0000"
plt.axis([0.0, 10.0, -0.5, 1.5 ] )
plt.plot(xg,u, 'b-')
plt.title(display)
plt.ylabel("U")
plt.xlabel("X")
plt.savefig(filename)
plt.show(block=False)
plt.pause(5.0)
plt.close()

#analytical solution after t=1.0
dt = dx
steps = 10
itermax = int ( 2.0/ dt ) + 1
iter = 1
while iter < itermax:
    for i in range(1, N-1):
        un[i] = u[i-1]

    t = iter * dt
    if (iter%steps == 0):
        num =str(iter)
        display = "t = %.4f"%(t)
        #filename = "f"+num.zfill(5)+".png"
        filename = "f-"+num+".png"
        plt.axis([0.0, 10.0, -0.5, 1.5 ] )
        plt.plot(xg,u, 'b-')
        plt.title(display)
        plt.ylabel("U")
        plt.xlabel("X")
        plt.savefig(filename)
        plt.clf()
    
    iter +=1
    u[:] = un[:]

'''
filename = "final.png"
display = "t = %.4f"%(t)
plt.axis([0.0, 10.0, -0.5, 1.5 ] )
plt.plot(xg,u, 'b-')
plt.title(display)
plt.ylabel("U")
plt.xlabel("X")
plt.savefig(filename)
plt.show(block=False)
plt.pause(5.0)
plt.close()
'''

