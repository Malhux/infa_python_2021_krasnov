import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10, 10.01, 0.01)
plt.plot (x, x**2-x-6, label=r'$y(x)=x^2-x-6$')
plt.xlabel (r'$x$')
plt.ylabel (r'$y(x)$')
plt.grid(True)
plt.legend()
plt.show()  #корни графически нашел x_1=-2 и x_2=3