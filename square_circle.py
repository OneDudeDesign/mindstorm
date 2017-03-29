import turtle


def draw_square(some_turtle):
    square_sides = 0
    while square_sides < 4:
        some_turtle.forward(100)
        some_turtle.right(90)
        square_sides = square_sides + 1


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(0)
    for i in range(1,361):
        draw_square(brad)
        brad.right(1)

    window.exitonclick()


draw_art()
