import turtle as t

t.screensize(300,300,'white')
t.hideturtle()
t.speed(10)
t.pensize(4)
t.pencolor('gold')
t.penup()
t.goto(0,-150)
t.pendown()
t.begin_fill()
t.fillcolor('gold')
t.circle(150,45)
t.left(90)
t.goto(75,-75)
t.penup()
t.goto(0,-150)
t.pendown()
t.right(135)
t.circle(150,-225)
t.right(90)
t.goto(75,75)
t.left(45)
t.goto(75,-75)
t.end_fill()

t.penup()
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
t.done()