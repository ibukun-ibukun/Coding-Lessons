import turtle

t = turtle.Turtle()

t.speed(3)

while True:
    print("\nDrawing Tool command:")
    print("f for forward")
    print("b for backward")
    print("l for left")
    print("r for right")
    print("q for quit")
    print("colours: red, orange, green, purple, blue")
    print("clear = wipe the screen")
    print("up = penup")
    print("down = pendown")
    command = input("\nEnter command (F/B/L/R/q)").lower().strip()

    if command == 'q':
        print("Bye!")
        break

    elif command == 'f':
        t.fd(50)

    elif command == 'b':
        t.bk(50)

    elif command == 'l':
        t.lt(90)

    elif command == 'r':
        t.rt(90) 

    elif command == "red":
        t.color("red")
        print("Pen changed to red")

    elif command == "orange":
        t.color("orange")
        print("Pen changed to orange")

    elif command == "green":
        t.color("green")
        print("Pen changed to green")

    elif command == "purple":
        t.color("purple")
        print("Pen changed to purple")

    elif command == "blue":
        t.color("blue")
        print("Pen changed to blue")  

    elif command == "clear":
        t.clear()
        print("screen cleared.")   
        
    elif command == "up":
        t.penup()
        print("Pen up!")

    elif command == "down":
        t.pendown()
        print("Pen down!")

    else:
        print("Invalid Command..")       


turtle.done
