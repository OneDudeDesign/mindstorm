import turtle


def draw_square(some_turtle):
    square_sides = 0
    while square_sides < 4:
        some_turtle.forward(100)
        some_turtle.right(90)
        square_sides = square_sides + 1


def draw_circle(some_turtle):
    some_turtle.circle(100)


def draw_triangle(some_turtle):
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.left(135)
    some_turtle.forward(141)
    some_turtle.left(135)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)
    draw_square(brad)

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    draw_circle(angie)

    todd = turtle.Turtle()
    todd.shape('triangle')
    todd.color('green')
    draw_triangle(todd)

    window.exitonclick()


draw_art()
