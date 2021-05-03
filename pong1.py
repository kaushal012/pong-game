import turtle

win = turtle.Screen()
win.title("pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#score
scorea = 0
scoreb = 0


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(+350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("light blue")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

#pen 
pen = turtle.Turtle()
pen.speed(1)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,270)
pen.write("player A: 0  Player B: 0", align="center", font=("courier", 12, "normal"))



#functions
def paddlea_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddlea_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddleb_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddleb_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)        

#keyboard inputs
win.listen()
win.onkeypress(paddlea_up, "w")
win.onkeypress(paddlea_down,"s")
win.onkeypress(paddleb_up , "Up")
win.onkeypress(paddleb_down, "Down")
#main game loop
while True:
    win.update()


    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0 , 0)
        ball.dx *= -1
        scorea += 1
        pen.clear()
        pen.write(f"player A: {scorea}  Player B: {scoreb}", align="center", font=("courier", 12, "normal"))

    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1
        scoreb += 1
        pen.clear()
        pen.write(f"player A: {scorea}  Player B: {scoreb}", align="center", font=("courier", 12, "normal"))

    #paddle ball collisions
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

        
    if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1





