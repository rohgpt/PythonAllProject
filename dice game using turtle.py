import random
import turtle

outcome = random.randint(1, 6)
draw = turtle.Turtle()
draw.width(5)
draw.color("green")
for i in range(4):
    draw.forward(100)
    draw.right(90)
draw.penup()
draw.hideturtle()
draw.right(90)
draw.forward(20)
draw.left(90)
draw.forward(50)
draw.pendown()
draw.fillcolor("green")
draw.showturtle()
print(outcome)
if outcome == 1:
    draw.right(140)
    draw.forward(20)
    draw.penup()
    draw.hideturtle()
    draw.backward(20)

    draw.left(140)
    draw.pendown()
    draw.showturtle()
    draw.right(90)
    draw.forward(70)

    draw.hideturtle()
    draw.right(90)
    draw.forward(20)
    draw.backward(40)
else:
    draw.hideturtle()
    draw.penup()
    draw.backward(15)
    draw.pendown()
    if outcome != 4:
        draw.forward(45)
        if outcome != 6 and outcome != 5:
            draw.right(90)
            draw.forward(35)
        else:
            draw.hideturtle()
            draw.penup()
            draw.right(90)
            draw.forward(35)
            draw.pendown()
            draw.showturtle()
    else:
        draw.hideturtle()
        draw.penup()
        draw.forward(45)
        draw.right(90)
        draw.showturtle()
        draw.pendown()
        draw.forward(35)

    draw.right(90)
    draw.forward(45)
    draw.right(90)
    if outcome == 6 or outcome == 5 or outcome == 4:
        draw.forward(35)
        draw.backward(35)
    if outcome != 2 and outcome != 6:
        draw.penup()
    draw.backward(35)
    draw.right(90)
    if outcome != 2 and outcome != 6:
        draw.pendown()
    if outcome == 4:
        draw.penup()
    draw.forward(45)
    draw.hideturtle()
    if outcome == 4:
        draw.pendown()
    if outcome == 2:
        draw.penup()
    draw.left(90)
    draw.forward(35)
    if outcome == 2:
        draw.pendown()
# draw.penup()
# draw.backward(20)
# draw.forward(45)
# draw.pendown()
# draw.right(90)
# draw.forward(70)
