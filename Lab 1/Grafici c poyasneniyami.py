import numpy as np                     # подключить библиотеку для вычисления мат. функций
import matplotlib.pyplot as plt        # подключить библиотеку для построения графиков
x = np.arange(-10, 10.01, 0.01)        # создать массив чисел от -10 включая до 10.01 не включая с шагом 0.01
plt.figure(figsize=(10, 5))            # задаем размеры окна, в котором выведется график: 10 по горизонтали, 5 по вертикали
plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')  # построить график синуса и подписать его в легенде
plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
plt.plot(x, -x, label=r'$f_3(x)=-x$')
plt.xlabel(r'$x$', fontsize=14)        # подписать ось икс шрифтом с размером 14   
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)                         # включить клеточную разметку
plt.legend(loc='best', fontsize=12)    # показывать легенду 
plt.savefig('grafic.png')              # сохранить график файлом
plt.show()                             # показать график