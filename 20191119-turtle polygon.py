import turtle as t

def polygon(n):
    for x in range(n):
          t.forward(50)
          t.left(360/n)

def polygon2(n, a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)

polygon(3)
polygon(4)

t.up()
t.forward(100)
t.down()

polygon2(3, 100)
polygon2(5, 100)
