import numpy as np
import matplotlib.pyplot as plt
b=input('Введите наименьший икс:')
c=input('Введите наибольший икс:')
d=input('Введите шаг:')
x=np.arange(float(b), float(c), float(d))
a=input('Введите функцию:')
with plt.xkcd():
    plt.figure(figsize=(10, 5))
    plt.plot (x, eval(a))
    plt.grid(True)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.show()