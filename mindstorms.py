import turtle

window = turtle.Screen()
window.bgcolor("red")


def draw_square():
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)

    square_sides = 0
    while square_sides < 4:
        brad.forward(100)
        brad.right(90)
        square_sides = square_sides + 1


draw_square()


def angie_circle():
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)


angie_circle()


def todd_triangle():
    todd = turtle.Turtle()
    todd.shape('triangle')
    todd.color('green')

    todd.forward(100)
    todd.left(90)
    todd.forward(100)
    todd.left(135)
    todd.forward(141)
    todd.left(135)


todd_triangle()

window.exitonclick()
