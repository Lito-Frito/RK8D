from termios import TIOCPKT_DOSTOP
import turtle
import random


def game_loop(playerA, playerB):

    wn = turtle.Screen()
    wn.title("Pong by @crc8109")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    # tracer stops window from updating; speeds our game up
    wn.tracer(0)

    # Score
    score_a = 0
    score_b = 0

    # Paddle A
    # TODO add bumper physics to dx where SPACEBAR adds horizontal momentum
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    # Tells Turtle not to draw a line as it moves
    paddle_a.penup()
    paddle_a.goto(-350, 0)


    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)


    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    # speed factor: random value between a certain range
    ball.dx = random.uniform(0.02, 0.04)
    ball.dy = random.uniform(0.02, 0.04)


    # Pen/Scorecard
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    # TODO  Add ability for users to pass along their names
    pen.write(f"{playerA}: 0 {playerB}: 0", align="center", font=("Courier", 24, "normal"))


    # Control Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 15
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 15
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 15
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 15
        paddle_b.sety(y)


    # Keyboard Binding
    wn.listen()

    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_up, "W")

    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_a_down, "S")

    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    game_not_over = True

    # Main game loop
    while game_not_over:

        wn.update()

        winning_goal = 5

        # Move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border boundary/physics

        # Top/Bottom boundaries
        if ball.ycor() > 290:
            # Reset ball to avoid any issues
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Left/Right boundaries
        if ball.xcor() > 350:
            # Reset upon scoring
            ball.goto(0, 0)
            ball.dy = -random.uniform(0.02, 0.04)
            ball.dx = -random.uniform(0.02, 0.04)
            score_a += 1
            # Resets scorecard each time score is updated
            pen.clear()
            pen.write("{}: {} {}: {}".format(playerA, score_a, playerB, score_b), align="center", font=("Courier", 24, "normal"))

            # if a winning goal is scored, terminate the game and let the players know who won
            if score_a >= 5:
                game_not_over = False
                pen.clear()
                pen.write(f"{playerA} wins!", align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -350:
            ball.goto(0, 0)
            ball.dy = random.uniform(0.02, 0.04)
            ball.dx = random.uniform(0.02, 0.04)
            score_b += 1
            pen.clear()
            pen.write("{}: {} {}: {}".format(playerA, score_a, playerB, score_b), align="center", font=("Courier", 24, "normal"))

            if score_b >= 5:
                game_not_over = False
                pen.clear()
                pen.write(f"{playerB} wins!", align="center", font=("Courier", 24, "normal"))

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50): # 50 ensures edges of paddle count as hits
            ball.setx(340)
            ball.dx *= -1.1
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
            ball.setx(-340)
            ball.dx *= -1.1

if __name__ == "__game_loop__":
    game_loop()