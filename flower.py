import turtle


def draw_petal(some_turtle):
    some_turtle.color('green')
    some_turtle.forward(100)
    some_turtle.left(60)
    some_turtle.color('blue')
    some_turtle.forward(100)
    some_turtle.left(120)
    some_turtle.forward(100)
    some_turtle.color('green')
    some_turtle.left(60)
    some_turtle.forward(100)


def draw_art():

    window = turtle.Screen()
    window.bgcolor('white')

    flower = turtle.Turtle()
    flower.shape('turtle')
    flower.speed(0)
    flower.window_height()

    for i in range(1,37):
        draw_petal(flower)
        flower.left(10)
    flower.color('red')

    flower.right(90)
    flower.penup()
    flower.forward(175)
    flower.pendown()
    flower.color('green')
    flower.forward(300)
    flower.left(180)

    window.exitonclick()

draw_art()