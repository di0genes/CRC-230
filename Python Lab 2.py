import turtle

window = turtle.Screen()
bug = turtle.Turtle()

window.setup(1500, 1000)
window.bgcolor("blue")
window.title("Look At My Beautiful Art")

bug.color("green")
bug.pensize(5)
#is bug.width(5) different somehow?
bug.speed(50)

bug.penup()
bug.goto(-900,0)
bug.pendown()

bug.fillcolor("green")
bug.begin_fill()



for i in range(6):
    bug.forward(2400)
    bug.right(90)

bug.end_fill()
