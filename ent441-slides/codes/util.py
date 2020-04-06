import numpy as np
import matplotlib.pyplot as plt

def printsomething():
    print("Something")

#display function
def runtime_display(display, u, x, xmin,xmax,ymin,ymax):
    plt.axis([xmin, xmax, ymin, ymax ] )
    plt.title(display)
    plt.ylabel("U")
    plt.xlabel("x")
    plt.plot(x,u,'bo-')
    plt.pause(0.001)
    plt.clf() #clear drawing
    return 0
