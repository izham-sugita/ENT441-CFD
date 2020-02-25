import numpy as np
import matplotlib.pyplot as plt

imax = 101
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

itermax = int( 2.0/dt ) 
c = 1.0
alpha = 0.5*c*dt/dx
beta = ( 0.5*c*dt/dx )



for iter in range(itermax):

    for i in range(1,imax-1):
        denominator = u[i+1] - u[i]
        numerator = u[i]-u[i-1]
        ratio = numerator / (denominator + 0.001)
        if denominator == 0.0:
            mm = 0.0
        if abs(ratio) > 0.0:
            mm = 1.0

        un[i] = u[i] - alpha*( u[i+1] - u[i-1] ) + mm*beta*(u[i-1] - 2.0*u[i] + u[i+1] )

    #update
    u = un
    plt.axis([0.0, 11.0, -0.5, 1.5 ] )
    plt.plot(x,u,'bo-')
    plt.pause(0.1)
    plt.clf() #clear drawing
    



plt.axis([0.0, 11.0, -0.5, 1.5 ] )
plt.plot(x,u, 'bo-')
plt.title("After advection")
plt.ylabel("u")
plt.show()

