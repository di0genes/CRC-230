import turtle


screen = turtle.Screen()
larry = turtle.Turtle()

screen.bgcolor("black")
screen.title("Tortoise!")

larry.color("red")
larry.width(5)
larry.speed(100)

for i in range(4):
    larry.forward(100)
    larry.left(90)
for i in range(3):
    larry.color("orange")
    larry.forward(100)
    larry.left(120)
for i in range(5):
    larry.color("yellow")
    larry.forward(100)
    larry.left(72)
for i in range (6):
    larry.color("green")
    larry.forward(100)
    larry.left(60)
    
#for i in range(360):
#    larry.color("blue")
#    larry.speed(10000)
#    larry.forward(2)
#    larry.left(1)

for i in range (1):
    larry.forward(50)
    larry.color("blue")
    larry.circle(100)




screen.exitonclick()
