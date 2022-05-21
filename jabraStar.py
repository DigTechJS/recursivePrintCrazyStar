import turtle

star=turtle.Turtle()
star.getscreen().bgcolor("#994444")
star.speed(0)

star.penup()
star.goto(-200,80)
star.pendown()
def stars(turtle,size):
    for i in range(5):
        if size<=10:
            return
        else:
            star.color("white","#ff8080")
            star.begin_fill()
            turtle.forward(size)
            stars(star,size/4)
            turtle.right(144)
            star.end_fill()
        i+=1
stars(star,360)
turtle.done()