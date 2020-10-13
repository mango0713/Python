
import turtle as ps

def turn_right() :
    ps.setheading(0)
    ps.forward(10)

def turn_up() :
    ps.setheading(90)
    ps.forward(10)

def turn_down() :
    ps.setheading(270)
    ps.forward(10)

def turn_left() :
    ps.setheading(180)
    ps.forward(10)

def blank() :
    ps.clesr()


ps.shape("turtle")
ps.speed(0)

ps.onkeypress (turn_right, "Right")
ps.onkeypress (turn_up, "Up")
ps.onkeypress (turn_down, "Down")
ps.onkeypress (turn_left, "Left")
ps.onkeypress (blank, "Escape")
ps.listen()
