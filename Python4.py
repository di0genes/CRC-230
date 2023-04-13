import random
import turtle

window = turtle.Screen()            #initialize variables
t = turtle.Turtle()
window.colormode(255)

bladecount = 0              
r = 0
b = 0

window = turtle.Screen()
t = turtle.Turtle()
t.speed(500)

window.setup(800, 800)
t.penup()
t.goto(-250, -250)
t.pendown()

for i in range(4):              #draw window
    t.forward(500)
    t.left(90)

t.penup()
t.goto (250, -250)              #go to starting point for grass
t.pendown()

lengthcount = [0]

for grass in range(10):         # for all the grass across the screen
    t.width(1)
    t.begin_fill()    
    for blade in range (1):             #for each blade of grass
        g = random.randint(100, 255)
        t.fillcolor(r, g, b)
        t.color(r, g, b)
        bladelength = random.randint(35, 40)
        t.left(90)
        t.forward(bladelength)
        t.left(90)
        t.forward(2)
        t.left(90)
        t.forward(bladelength)
        t.left(90)
        for grass in range (1):                 #count each blade of grass and add it to the list "lengthcount"
            lengthcount.append(bladelength)
    t.end_fill()
t.forward(bladelength)

def occurrences(lengthcount, x):                #count the blade lengths
    count = 0
    for n in lengthcount:
        if (n == x):
            count = count + 1
    return(count)

e1 = 35                                         #Organize blade lengths
e2 = 36
e3 = 37
e4 = 38
e5 = 39
e6 = 40

print("35: " + str(occurrences(lengthcount, e1)))   # List counts of each length       
print("36: " + str(occurrences(lengthcount, e2)))
print("37: " + str(occurrences(lengthcount, e3)))
print("38: " + str(occurrences(lengthcount, e4)))
print("39: " + str(occurrences(lengthcount, e5)))
print("40: " + str(occurrences(lengthcount, e6)))
