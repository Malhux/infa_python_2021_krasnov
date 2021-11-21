import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-25, 25.01, 0.01)
a=x**2+1
b=1/(1+np.sin(x)**2)
c=1+np.tan(b)
d=np.log(a)/np.log(c)
e=-np.abs(x)/10
f=np.e**e*d
plt.plot (x, f)
plt.grid(True)
plt.xlabel (r'$x$')
plt.ylabel (r'$f(x)$')
plt.show()