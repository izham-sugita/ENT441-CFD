import numpy as np
import matplotlib.pyplot as plt
import random

x = np.array( [4.0,5.0,6.0,7.0,8.0] )
fx = (x+0.01*random.random() )*(x+0.01*random.random()) \
- 4.0*(x+0.01*random.random()) \
+ (3.0+0.01*random.random())

print(x)
print(fx)

print("Calculate linear fitting by least square method")

print(len(x))

A = np.ndarray((2,2))
xv = np.ndarray((2))
b = np.ndarray((2))

A[0][0] = np.sum( x*x )
A[0][1] = np.sum( x )
A[1][0] = np.sum( x )
A[1][1] = float(len(x) )

b[0] = np.sum( x*fx )
b[1] = np.sum( fx )

xv = np.matmul( np.linalg.inv(A), b )
#xv2 = np.dot(np.linalg.inv(A), b)

print(xv)
#print(xv2)

fdash = xv[0]*x + xv[1]
print(x)
print(fdash)

coef = np.polyfit(x, fx, 4)
fpoly = coef[0]*x**4 + coef[1]*x**3 + coef[2]*x**2 \
        + coef[3]*x + coef[4]



plt.axis([3.0, 9.0, -2.0, 40.0] )
plt.plot(x,fx, 'bo')
plt.plot(x,fdash, 'k-')
plt.plot(x,fpoly, 'b-')
plt.xlabel('x')
plt.ylabel( 'f(x)' )
plt.show()

