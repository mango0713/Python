import turtle as t

def tri(length) :
      if length <= 10 :
           for i in range(0,3) :
                 t. forward(length)
                 t.left(120)
           return
      new_length = length / 2
      tri(new_length)
      t.forward(new_length)
      tri (new_length)
      t.backward(new_length)
      t.left(60)
      t.forward(new_length)
      t.right(60)
      tri (new_length)
      t.left(60)
      t.backward(new_length)
      t.right(60)

t.speed(0)
tri(20)
