from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(height=500, width=500)
y = [-70, -40, -10, 20, 50, 80]
colors = ['red', 'green', 'blue', 'yellow', 'violet', 'maroon']
turtles = []
is_race_on = False
for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y[i])
    # here we are storing address of the new turtle which is being created, not the value
    turtles.append(new_turtle)

user_bet = screen.textinput(title="Turtle Race Game", prompt="Which title would win the race? (Enter the colour) :")
if user_bet:
    is_race_on = True

while is_race_on:
    win_color = ''
    for i in range(0, 6):
        turtles[i].forward(random.randint(0, 10))
        turtle_position = turtles[i].position()
        if turtle_position[0] > 230:
            win_color = colors[i]
            is_race_on = False

if win_color == user_bet :
    print(f"You win! {user_bet} won the race")
else:
    print(f"You lose! {win_color} won the race")


screen.exitonclick()
