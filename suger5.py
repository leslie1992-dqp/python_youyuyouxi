import turtle as t

t.screensize(300,300,'white')
t.hideturtle()
t.speed(10)


t.penup()
t.begin_fill()
t.fillcolor('gold')
t.goto(-75,75)
t.down()
t.pensize(5)
t.pencolor('darkorange')
t.goto(75,75)
t.right(90)
t.goto(75,-75)
t.right(90)
t.goto(-75,-75)
t.right(90)
t.goto(-75,75)
t.end_fill()
t.done()