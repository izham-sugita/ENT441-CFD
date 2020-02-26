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
x = np.ndarray((imax),dtype=np.float64)

for i in range(imax):
    x[i] = i*dx
    u[i] = 0.0
    if x[i] > 2.0 and x[i] < 4.0:
        u[i] = 1.0

'''
plt.plot(x, u, 'ko-')
plt.title('Initial condition')
plt.ylabel('u')
plt.show()
'''

un = u #initiate new value for u
dt = np.float64(input("Enter dt, dx=%s\n  "%dx ))

itermax = int( 1.0/dt ) 

c = 1.0
alpha = 0.5*c*dt/dx
beta = ( 0.5*c*dt/dx )



for iter in range(itermax):

    for i in range(1,imax-1):
        denominator = u[i+1] - u[i]
        numerator = u[i]-u[i-1]
        ratio = numerator / (denominator + 0.001)
        mm = 0.0
        if abs(ratio) > 1.0:
            mm = 1.0
        else:
            mm = 0.0 #ratio

        un[i] = u[i] - alpha*( u[i+1] - u[i-1] ) + mm*beta*(u[i-1] - 2.0*u[i] + u[i+1] )
        #un[i] = u[i] - 2.0*alpha*( u[i] - u[i-1] ) #1st upwind

    #update
    u = un
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


