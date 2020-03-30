import numpy as np
import matplotlib.pyplot as plt

#Changing the default size
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 20
fig_size[1] = 16
plt.rcParams["figure.figsize"] = fig_size

imax = 1001
dx = 10.0/(imax-1)
u = np.ndarray((imax),dtype=np.float64)
un = np.ndarray((imax),dtype=np.float64)
u1 = np.ndarray((imax),dtype=np.float64)
x = np.ndarray((imax),dtype=np.float64)

for i in range(imax):
    x[i] = i*dx
    u[i] = 0.0
    if x[i] > 4.0 and x[i] < 6.0:
        u[i] = 1.0

        
#copy value; not the same object
u1[:] = u[:]
un[:] = u[:] 
dt = np.float64(input("Enter dt, dx=%s\n  "%dx ))

itermax = int( 1.0/dt ) 

c = 1.0
c = float( input("Enter c, -1.0 or 1.0:\n") )

alpha = c*dt/dx

for iter in range(itermax):

    for i in range(1,imax-1):
        
        u1[i] = u[i] - alpha*(u[i] - u[i-1] )

    for i in range(1,imax-1):
        
        un[i] = 0.5*( u[i] + u1[i] ) - 0.5*alpha*( u1[i+1] - u1[i] )

    #update by copying value
    u[:] = un[:]
    current = iter*dt + dt
    display = "t = %.4f"%(current)
    plt.axis([0.0, 10.0, -0.5, 1.5 ] )
    plt.title(display)
    plt.ylabel("U")
    plt.xlabel("x")
    plt.plot(x,u,'bo-')
    plt.pause(0.001)
    plt.clf() #clear drawing
    

filename = "final.png"
plt.axis([0.0, 10.0, -0.5, 1.5 ] )
plt.plot(x,u, 'bo-')
plt.title(display)
plt.ylabel("U")
plt.xlabel("x")
plt.savefig(filename)
plt.show()


