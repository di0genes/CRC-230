import random
import turtle

window = turtle.Screen()    # Set up screen
window.setup(600,600)
window.colormode(255)       # Make color mode 255
t = turtle.Turtle()         # Shorten command
t.width(2)                  # Size up pen



for i in range(10):
    t.penup()
    randcoordx = random.randint(-250, 250) # Coordinates
    randcoordy = random.randint(-250, 250)
    randsize = random.randint(10, 150)      # Triangle sizes
    randr = random.randint(0, 0)  # Color choices for triangles
    randg = random.randint(20, 255)
    randb = random.randint(0, 0)
    randrw = random.randint(0, 255) # Color choices for window
    randgw = random.randint(0, 255)
    randbw = random.randint(0, 255)
    window.bgcolor(randrw, randgw, randbw)
    t.goto(randcoordx,randcoordy)
    t.color(randr, randg, randb) # Choose color for fill
    t.fillcolor(randr, randg, randb) # Assign color to fill
    t.begin_fill()   

    for side in range(3):       # Make a triangle
        t.pendown()
        t.forward(randsize)
        t.left(120)
        t.penup()
    t.end_fill()
    t.hideturtle()              # Hide that nub
