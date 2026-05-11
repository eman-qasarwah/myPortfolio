import turtle


def draw(color, sides, length, angle, distance):
    eman = turtle.Turtle()
    eman.speed(0)
    eman.width(6)
    eman.penup()
    eman.color(color)
    eman.left(angle)
    eman.forward(distance)
    eman.pendown()

    for _ in range(sides):
        eman.forward(length)
        eman.right(144)

    eman.hideturtle()


for angle in [180, 135, 90, 45, 0]:
    draw("red", 5, 50, angle, 100)

for angle in [180, 135, 90, 45, 0]:
    draw("blue", 5, 30, angle, 60)

for angle in [180, 135, 90, 45, 0]:
    draw("yellow", 5, 5, angle, 30)


turtle.done()
