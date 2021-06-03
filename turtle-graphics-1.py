import turtle
import math
import random 
#mega man 24 high 32 wide


twin = turtle.Screen()
twin.clear()
t = turtle.Turtle()
#tWin = turtle.Screen()
t.penup()
t.goto(450,400)
t.pendown()   
t.color("#C32148")
t.width(50)
t.goto(-450,400)
t.goto(-100,100)
t.goto(-100,-100)
t.goto(100,-100)
t.goto(100,100)
t.goto(450,400)
t.penup()
t.goto(0,0)
twin.exitonclick()
