import turtle
import time

t = turtle.Pen()
def eye():
        
    for i in range(80):
        t.color('#0000CD')
        
        t.forward(3)
        t.left(5)


for i in range(36):
    t.color('#FFD700')
    
    t.forward(30)
    t.left(10)
t.up()
t.left(90)
t.forward(250)
t.left(90)
t.forward(50)
t.down()
eye()

t.left(120)

t.up()
t.forward(150)
t.down()
eye()
t.up()
t.left(90)
t.back(150)
t.down()

for i in range(10):
    t.color('#8B0000')
    
    t.forward(25)
    t.left(15)



