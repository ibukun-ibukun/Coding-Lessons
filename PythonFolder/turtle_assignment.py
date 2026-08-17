import turtle
turtle.bgcolor("sky blue")

t = turtle.Turtle()

"""Triangle for roofing"""
t.color("brown")

for i in range(3):
    t.forward(120)
    t.left(120)

t.right(90)  

"""Square for the main house"""
t.color("purple")
for i in range(4):
    t.forward(120)
    t.left(90)

t.forward(120)
t.left(90) 

"""Door"""
t.color("dark blue")
t.forward(45)
t.left(90)

t.forward(65)
t.right(90)

t.forward(45)
t.right(90)

t.forward(65)

t.right(90)

"""Grass"""
t.color("dark green")
t.forward(400)
t.backward(600)

t.penup()
t.forward(285)
t.right(90)
t.forward(75)
t.right(90)
t.forward(25)
t.left(90)

t.pendown()

"""Windows"""
t.color("black")
for i in range(4):
    t.forward(20)
    t.left(90)

t.penup()
t.forward(20) 
t.right(90)
t.forward(55)

t.pendown()

for i in range(4):
    t.forward(20)
    t.right(90)

t.penup()
t.forward(200)
t.right(90)
t.forward(100)
t.right(180)

t.forward(300)
t.pendown()
t.left(36)

"""Stars"""
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