import turtle as t
t.shape('turtle')
t.speed(5)
t.right(180)
t.penup()
t.goto(70,0)
t.pendown()
def ugol(n):                         # черепаха рисует правильный n-угольник со стороной в 12 раз больше количества углов
    for i in range(n):
        t.forward(12*n)
        t.left(180-180*(n-2)/n)
for j in range (3,13):
	t.right(180 * (j - 2) / j / 2)
	ugol(j)
	t.left(180 * (j - 2) / j / 2)
	t.penup()
	t.backward(17)
	t.pendown()