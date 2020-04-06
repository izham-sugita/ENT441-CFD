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

def save_anim(filename, display, u, x, xmin, xmax, ymin, ymax):
    plt.axis([xmin, xmax, ymin, ymax ] )
    plt.plot(x,u, 'bo-')
    plt.title(display)
    plt.ylabel("U")
    plt.xlabel("x")
    plt.savefig(filename)

    

#Changing the default size
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 20
fig_size[1] = 16
plt.rcParams["figure.figsize"] = fig_size

imax = 101
dx = 1.0/(imax-1)
u = np.ndarray((imax),dtype=np.float64)
un = np.ndarray((imax),dtype=np.float64)
x = np.ndarray((imax),dtype=np.float64)

for i in range(imax):
    x[i] = i*dx
    u[i] = np.sin( x[i]*np.pi )
    un[i] = np.sin( x[i]*np.pi )


filename = "diff_init.png"
display = "t=0.000"
save_anim(filename, display, u, x, 0.0, 1.0, -0.1, 1.1)

dt = np.float64(input("Enter dt, dx=%s (dt is propotional to dx*dx) "%dx ))
itermax = np.int64( 0.5/dt ) +1
print("Maximum iteration: ", itermax)
kappa = 0.25 #diffusion coefficient
alpha = kappa * dt /(dx**2)
steps = itermax/1000
for iter in range(itermax):
    for i in range(1,imax-1):
        un[i] = u[i] + alpha*( u[i-1] - 2.0*u[i] + u[i+1] )
    #update
    u[:] = un[:]
    
    current = iter*dt + dt
    display = "t = %.4f"%(current)
    num = str(iter)
    filename = "f"+num.zfill(5)+".png"
    #util.runtime_display(display, u, x, 0.0, 15.0, -0.5, 1.5)
    if iter%steps == 0:
    #    save_anim(filename, display, u, x, -0.2, 1.2, -0.5, 1.5)
        runtime_display(display, u, x, -0.2, 1.2, -0.5, 1.5)


filename = "final_steps.png"
display = "t=%.4f"%(current)
save_anim(filename, display, u, x, 0.0, 1.0, -0.1, 1.1)


