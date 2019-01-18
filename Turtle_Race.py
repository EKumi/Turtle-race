from turtle import *
from random import randint
penup()
goto(-140,140)

speed(3.5)
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
    

bea=Turtle()
bea.color('red')
bea.shape('turtle')
bea.penup()
bea.goto(-160,100)
bea.pendown()


bob=Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,80)
bob.pendown()


fred=Turtle()
fred.color('orange')
fred.shape('turtle')
fred.penup()
fred.goto(-160,60)
fred.pendown()


linda=Turtle()
linda.color('yellow')
linda.shape('turtle')
linda.penup()
linda.goto(-160,40)
linda.pendown()


kofie=Turtle()
kofie.color('magenta')
kofie.shape('turtle')
kofie.penup()
kofie.goto(-160, 20)
kofie.pendown()

for turn in range(10):
    bea.right(36)
    bob.right(36)
    fred.right(36)
    linda.right(36)
    kofie.right(36)
for turn in range(100):
     bea.forward(randint(1,5))
     bob.forward(randint(1,5))
     fred.forward(randint(1,5))
     linda.forward(randint(1,5))
     kofie.forward(randint(1,5))            
