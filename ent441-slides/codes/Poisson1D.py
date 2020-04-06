import numpy as np
import matplotlib.pyplot as plt
import util

#display function
def runtime_display(display, u, x, xmin,xmax,ymin,ymax):
    plt.axis([xmin, xmax, ymin, ymax ] )
    plt.title(display)
    plt.ylabel("U")
    plt.xlabel("x")
    plt.plot(x,u,'bo-')
    plt.pause(0.001)
    plt.clf() #clear drawing

def save_anim(filename, display, color, u, x, xmin, xmax, ymin, ymax):
    plt.axis([xmin, xmax, ymin, ymax ] )
    plt.plot(x,u, color)
    plt.title(display)
    plt.ylabel("U")
    plt.xlabel("x")
    plt.savefig(filename)
    #plt.clf()

    
#Changing the default size
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 20
fig_size[1] = 16
plt.rcParams["figure.figsize"] = fig_size

imax = 101
dx = 1.0/(imax-1)
u = np.ndarray((imax),dtype=np.float64)
un = np.ndarray((imax),dtype=np.float64)
source = np.ndarray((imax),dtype=np.float64)
x = np.ndarray((imax),dtype=np.float64)

for i in range(imax):
    x[i] = i*dx
    u[i] = 0.0
    un[i] = 0.0
    source[i] = np.sin( x[i]*np.pi )


#filename = "diff_init.png"
#display = "t=0.000"
#save_anim(filename, display, u, x, 0.0, 1.0, -0.1, 1.1)

dt = np.float64(input("Enter dt, dx=%s (dt is propotional to dx*dx) "%dx ))
itermax = 100000
print("Maximum iteration: ", itermax)

alpha = dt /(dx**2)
steps = itermax/100
eps = 1.0e-7

for iter in range(1,itermax):
    for i in range(1,imax-1):
        un[i] = u[i] + alpha*( u[i-1] - 2.0*u[i] + u[i+1] ) - dt*source[i]
        
    #check for convergence
    resid = 0.0
    for i in range(1, imax-1):
        resid += ( un[i] - u[i] )**2

    if iter == 1:
        resid1 = np.sqrt( resid ) /( imax-2)

    resid = np.sqrt(resid)/ (imax-2)
    resid = resid / resid1

    if resid < eps:
        print("Steps : %d, Residual = %.4e"%(iter, resid) )
        print("Converged")
        break
          
    #update    
    u[:] = un[:]


    current = iter*dt + dt
    if iter%steps == 0:
        print("Steps : %d, Residual = %.4e"%(iter, resid) )

        
    #update residual
    resid1 = resid


filename = "Poisson_final_steps.png"
display = "t=%.4f"%(current)
color = 'bo'
save_anim(filename, display, color,  u, x, 0.0, 1.0, -0.12, 0.05)

color = 'k-'
filename = "Poisson_analytical.png"
display = "Analytical solution"
un[:] = -(1.0/(np.pi**2)) * np.sin(np.pi*x[:] )
save_anim(filename, display, color,  un, x, 0.0, 1.0, -0.12, 0.05)
