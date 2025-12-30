from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)

colors = ["red", "orange", "blue", "violet", "brown", "black"]

msg = Turtle()
msg.hideturtle()
msg.penup()
msg.goto(0, 200)
msg.color("red")

bet = None               
is_bet = True
is_race_on = False

while is_bet:
    bet = screen.textinput(
        title="Make your bet",
        prompt=f"Which turtle will win the race? {', '.join(colors)}"
    )

    if bet is None:
        screen.bye()
        break

    bet = bet.lower()

    if bet in colors:
        msg.clear()
        is_bet = False
        is_race_on = True
    else:
        msg.clear()
        msg.write(
            "Invalid color!\nChoose one of:\n" + ", ".join(colors),
            align="center",
            font=("Arial", 16, "bold")
        )


if not is_race_on:
    screen.exitonclick()
else:
    turtles = []
    x = -290
    y = -120

    for i in range(6):
        t = Turtle(shape="turtle")
        t.color(colors[i])
        t.penup()
        t.goto(x, y)
        turtles.append(t)
        y += 50

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 280:
                is_race_on = False
                winner = turtle.pencolor()

                if winner == bet:
                    print(f"You have won! The {winner} turtle is the winner!")
                else:
                    print(f"You have lost! The {winner} turtle is the winner!")

                break

            turtle.forward(random.randint(0, 10))
