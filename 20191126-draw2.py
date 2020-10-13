import turtle as p

p.bgcolor("black")
p.speed(0)

for x in range(300000) :
      if x % 3 == 0:
            p.color("cyan")
      if x % 3 == 1:
            p.color("magenta")
      if x % 3 == 2:
            p.color("lavender")
      p.forward(x * 0.5)
      p.left(179)
            
             

      



