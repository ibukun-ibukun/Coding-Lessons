import turtle

t = turtle.Turtle()

t.speed(3)

while True:
    print("Drawing Tool command:")
    print("f for forward")
    print("b for backward")
    print("l for left")
    print("r for right")
    print("q for quit")
    print("colours: red, orange, green, purple, brown, pink, yellow, blue")
    command = input("Enter command (F/B/L/R/q)").lower().strip()

    if command == 'q':
        break
    elif command == 'f':
        t.fd(50)
    elif command == 'b':
        t.bk(50)
    elif command == 'l':
        t.lt(90)
    elif command == 'r':
        t.rt(90) 
    elif command in ["red", "orange", "purple", "brown", "pink", "yellow", "blue"]:
        t.color(command)    
    else:
        print("Invalid Command..")       


turtle.done
