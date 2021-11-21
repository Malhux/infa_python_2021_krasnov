#Лекция №3 

def f(x):
    return x**2               # f = lambda x: x**2
def g(x):
    return x+10
def h(x):
    return x*1000
x=float(input('Введите число'))
for foo in f, g, h:
    print('Значение функции', foo(x))

#   Смысл функций
#   1) "подсушивание" кода - "снизу вверх"
#   2) формализация подзадач (документация / самодокументирующийся код!) - "сверху вниз"
#        -название
#        -параметры
#        -результат

def gen(option):
    def foo(x):
        return x+1
    def bar(x):
        return x*2