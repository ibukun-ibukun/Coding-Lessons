import turtle

t = turtle.Turtle()

t.color("orange")
t.speed(1)
#movement
for i in range(5):
    t.forward(150)
    t.right(144)



"""SQUARE
for i in range(4):
    t.right(90)
    t.forward(101)
t.penup()
t.forward(150)
t.pendown()TRIANGLE
for i in range(3):
    t.right(120)
    t.forward(100)
t.penup()
t.left(90)
t.forward(150)
t.pendown() PENTAGON   
for i in range(5):
    t.right(72)
    t.forward(100)

t.forward(100)
t.penup()
t.color("pink")
t.forward(100)
t.pendown()
t.forward(120)
t.right(90)
t.forward(120)

t.back(100)

t.right(90)
#t.left(90)

t.forward(100)
t.right(90)
t.left(90)
t.penup()
t.backward(100)
"""
#STARS

t.penup()
t.right(90)
t.forward(300)
t.pendown()

t.left(36)
t.color("orange")
for i in range(5):
    t.forward(20)
    t.right(144)

t.left(90)    
t.penup()
t.forward(100)

t.pendown()
for i in range(5):
    t.forward(60)
    t.right(144)

t.right(90)    
t.penup()
t.forward(100)

t.pendown()
for i in range(5):
    t.forward(20)
    t.right(144)

t.left(90)    
t.penup()
t.forward(100)  

t.pendown()
for i in range(5):
    t.forward(30)
    t.right(144)

t.right(90)    
t.penup()
t.forward(100)  

t.pendown()
for i in range(5):
    t.forward(40)
    t.right(144) 

t.left(90)    
t.penup()
t.forward(100)  

t.pendown()
for i in range(5):
    t.forward(20)
    t.right(144)  

t.right(90)    
t.penup()
t.forward(100)  

t.pendown()
for i in range(5):
    t.forward(40)
    t.right(144) 

t.left(90)    
t.penup()
t.forward(100)  

t.pendown()
for i in range(5):
    t.forward(30)
    t.right(144)  

t.left(90)    
t.penup()
t.forward(100)  

t.pendown()
for i in range(5):
    t.forward(30)
    t.right(144)

t.right(90)    
t.penup()
t.forward(100)  

t.pendown()
for i in range(5):
    t.forward(70)
    t.right(144)


turtle.done()
