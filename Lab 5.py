import turtle

tur = turtle.Turtle()
turtle.screensize(500,500)
tur.width(3)

bgrndcolor = int(input("What color would you like the background to be? \nYour options are \n1. Red \n2. Orange \n3. Yellow \n4. Green \n5. Blue \n6. Purple. \nPlease select a number. "))
facecolor = int(input("What color would you like the face to be? \nYour options are \n1. Red \n2. Orange \n3. Yellow \n4. Green \n5. Blue \n6. Purple. \nPlease select a number. "))
mood = input("Choose either: A. Happy or B. Sad : ")
name = input("What would you like to name it? : ")

if bgrndcolor == 1:
    turtle.bgcolor("red")
elif bgrndcolor == 2:
    turtle.bgcolor("orange")
elif bgrndcolor == 3:
    turtle.bgcolor("yellow")
elif bgrndcolor == 4:
    turtle.bgcolor("green")
elif bgrndcolor == 5:
    turtle.bgcolor("blue")
elif bgrndcolor == 6:
    turtle.bgcolor("purple")
else:
    print("Invalid choice.")



def eye(color, radius):
    tur.width(3)
    tur.down()
    tur.fillcolor(color)
    tur.begin_fill()
    tur.circle(radius)
    tur.end_fill()
    tur.up()


if facecolor == 1:
    tur.fillcolor("red")
elif facecolor == 2:
    tur.fillcolor("orange")
elif facecolor == 3:
    tur.fillcolor("yellow")
elif facecolor == 4:
    tur.fillcolor("green")
elif facecolor == 5:
    tur.fillcolor("blue")
elif facecolor == 6:
    tur.fillcolor("purple")
else:
    print("Invalid choice.")

tur.begin_fill()
tur.circle(100)
tur.end_fill()
tur.up()

tur.goto(-40, 120)
eye('black', 15)
tur.goto(40, 120)
eye('black', 15)


if mood == "A" or mood=="a":
    tur.goto(-40, 85)
    tur.down()
    tur.right(90)
    tur.circle(40, 180)
    tur.up()
elif mood == "B" or mood == "b":
    tur.goto(-40, 45)
    tur.down()
    tur.right(90)
    tur.circle(40, -180)
    tur.up()
else:
    print("Invalid choice.")

tur.goto(-50, -60)
tur.write((name), font=('Papyrus', 24, 'normal'))
