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
u1 = np.ndarray((imax),dtype=np.float64)
u2 = np.ndarray((imax),dtype=np.float64)
un = np.ndarray((imax),dtype=np.float64)
x = np.ndarray((imax),dtype=np.float64)

for i in range(imax):
    x[i] = i*dx
    u[i] = 0.0
    if x[i] > 2.0 and x[i] < 4.0:
        u[i] = 1.0


#not the same object; just copy value 
u1[:] = u[:]
u2[:] = u[:]
un[:] = u[:] 
dt = np.float64(input("Enter dt, dx=%s\n  "%dx ))

itermax = int( 1.0/dt ) 

c = 1.0

c = float( input("Enter c, -1 or 1 ") )

alpha = 0.5*c*dt/dx
beta = ( 0.5*c*dt/dx )
g1 = 0.5
g2 = 0.5
eps = 1.0e-4

for iter in range(itermax):

    for i in range(1,imax-1):
                
        dudx_mhalf = (u[i]-u[i-1])/dx
        dudx_phalf = (u[i+1]-u[i])/dx

        u1[i] = u[i] - 0.5*c*dt*( g1*dudx_mhalf + g2*dudx_phalf  )

    for i in range(1,imax-1):
                
        dudx_mhalf = (u1[i]-u1[i-1])/dx
        dudx_phalf = (u1[i+1]-u1[i])/dx

        un[i] = u[i] - c*dt*( g1*dudx_mhalf + g2*dudx_phalf  )

    
    #update
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
    

#filename= "t%.2f"%(current) + ".png"
filename = "final.png"
plt.axis([0.0, 10.0, -0.5, 1.5 ] )
plt.plot(x,u, 'bo-')
plt.title(display)
plt.ylabel("U")
plt.xlabel("x")
plt.savefig(filename)
plt.show()


