import turtle as t
t.shape('turtle')
t.speed(100)
t.color('green')
t.width(3)
def okrL(a):                                  #опишем функцию, заставляющую черепашку рисовать окружность c поворотом против часовой стрелки
    for i in range(1000):                     #(предел правильного n-угольника при n, стремящемся к бесконечности) через правильный 1000-угольник со стороной a
        t.forward(a)
        t.left(180-180*998/1000)
for j in range(3):
    okrL(0.9)
    t.right(180)
    okrL(0.9)
    t.left(240)