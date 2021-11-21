import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.polynomial import polyfit
x=[11, 20, 34, 42, 53, 65, 77, 90, 106]
y=[20, 45, 65, 78, 90, 120, 135, 150, 178]
k1 = np.polyfit(x, y, deg=1)                      #возвращает коэффициенты многочлена заданной степени на основе апроксимации заданных точек (МНК)
f1 = np.poly1d(k1)                                #автоматически возвращает функцию апроксимирующего полинома
k2 = np.polyfit(x, y, deg=2)
f2 = np.poly1d(k2)

y1=[5, 17, 32, 48, 19, 22, 50, 70, 100]
k11 = np.polyfit(x, y1, deg=1)
f11 = np.poly1d(k11)
k22 = np.polyfit(x, y1, deg=2)
f22 = np.poly1d(k22)

#subplot 1
sp = plt.subplot(1, 3, 1) 
plt.plot(x, f1(x))
plt.errorbar(x, y, xerr=3.5, yerr=7)
plt.grid(True)
plt.title(r'$polyfit_1$')

#subplot 2
sp = plt.subplot(1, 3, 2)
plt.plot(x, f2(x))
plt.errorbar(x, y, xerr=3.5, yerr=7)
plt.grid(True)
plt.title(r'$polyfit_2$')

#subplot 3
sp = plt.subplot(1, 3, 3)
plt.plot(x, f11(x), label=r'$polyfit_11$')
plt.plot(x, f22(x), label=r'$polyfit_22$')
plt.errorbar(x, y1, xerr=3.5, yerr=7)
plt.grid(True)
plt.legend()
plt.title(r'$polyfits_y1$')

plt.show()