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
x = np.ndarray((imax),dtype=np.float64)

for i in range(imax):
    x[i] = i*dx
    u[i] = 0.0
    un[i] =0.0
    if x[i] > 4.0 and x[i] < 6.0:
        u[i] = 1.0
        un[i]=1.0

dt = np.float64(input("Enter dt, dx=%s\n  "%dx ))
itermax = int( 1.0/dt ) 
c = 1.0
c = float(input("Enter c, +1.0 or -1.0 "))
alpha = 0.5*c*dt/dx
kappa = 0.5*abs(c)*(dx/dt)
beta = kappa*( (dt**2)/(dx**2) )
eps = 1.0e-6

for iter in range(itermax):

    for i in range(1,imax-1):
        #controlling the artificial viscosity strength by using slope ratio
        # ratio = (u[i] - u[i-1]) / (u[i+1] - u[i])
        # the ratio should be 0<=ratio<=1.0 to avoid spurious oscillation
        
        num = (u[i] - u[i-1])
        denum = (u[i+1] - u[i] )
        ratio = num / (denum + eps) #eps to avoid zero division
        if ratio < 0.0 or ratio > 1.0:
            mm = 1.0 #choosing mm=1.0 revert to first order upwind
        else:
            mm = 0.0
        
        un[i] = u[i] - alpha*( u[i+1] - u[i-1] ) + mm*beta*(u[i-1] - 2.0*u[i] + u[i+1] )

    #update
    u[:] = un[:]

    current = iter*dt + dt
    display = "t = %.4f"%(current)
    plt.axis([0.0, 10.0, -0.5, 1.5 ] )
    plt.title(display)
    plt.ylabel("U")
    plt.xlabel("x")
    plt.plot(x,u,'b-')
    plt.pause(0.001)
    plt.clf() #clear drawing
    

filename = "final.png"
plt.axis([0.0, 10.0, -0.5, 1.5 ] )
plt.plot(x,u, 'b-')
plt.title(display)
plt.ylabel("U")
plt.xlabel("x")
plt.savefig(filename)
plt.show(block=False)
plt.pause(3)
plt.close()


