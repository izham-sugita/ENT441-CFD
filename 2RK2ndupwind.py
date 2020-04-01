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
    un[i] = 0.0
    if x[i] > 2.0 and x[i] < 4.0:
        #u[i] = 1.0
        #un[i] = 1.0
        u[i] =  np.sin( np.pi*0.5*( x[i]-2.0 ) )
        un[i] =  np.sin( np.pi*0.5*( x[i]-2.0 ) )
        u1[i] =  np.sin( np.pi*0.5*( x[i]-2.0 ) )

dt = np.float64(input("Enter dt, dx=%s\n  "%dx ))
itermax = int( 1.0/dt ) 
c = 1.0
alpha = c*dt/dx

up = int(np.sign(c))
print(up)

for iter in range(itermax):

    for i in range(1,imax-1):
        iup = i - int(np.sign(c))
        iup2 = i - 2*int(np.sign(c))
        u1[i] = u[i] -  0.5*alpha*0.5*( 3.0*u[i] -4.0*u[iup] + u[iup2] )

    for i in range(1,imax-1):
        iup = i - int(np.sign(c))
        iup2 = i - 2*int(np.sign(c))
        un[i] = u[i] -  alpha*0.5*( 3.0*u1[i] -4.0*u1[iup] + u1[iup2] )

    #update, make sure its a copy; not the same object
    u[:] = un[:]
    
        
    current = iter*dt + dt
    display = "t = %.4f"%(current)
    plt.axis([0.0, 15.0, -0.5, 1.5 ] )
    plt.title(display)
    plt.ylabel("U")
    plt.xlabel("x")
    plt.plot(x,u,'b-')
    plt.pause(0.001)
    plt.clf() #clear drawing
    

#filename= "t%.2f"%(current) + ".png"
filename = "final.png"
plt.axis([0.0, 15.0, -0.5, 1.5 ] )
plt.plot(x,u, 'b-')
plt.title(display)
plt.ylabel("U")
plt.xlabel("x")
plt.savefig(filename)
plt.show()


