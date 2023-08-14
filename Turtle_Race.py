from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
# Adding a Popup
user_bet = screen.textinput(title = 'Make your bet!', prompt = 'Which turtle will win the race?')
colors = ['red', 'green', 'blue', 'yellow', 'purple']
distance = [-100, -50, 0, 50, 100]
turtles = []
should_continue = False

# Create 5 turtles and align them
for i in range(len(colors)):
    name = colors[i]
    name = Turtle(shape='turtle')
    name.penup()
    name.goto(x=-230, y=distance[i])
    name.color(colors[i])
    turtles.append(name)

# Start the Race
if user_bet:
    should_continue = True

while should_continue:
    for my_turtle in turtles:
        my_turtle.forward(random.randint(0, 10))

        # End the Race
        if my_turtle.xcor() > 220:
            should_continue = False

        # Show the Result
            screen.setup(width=50, height=50)
            screen.title('RESULTS')
            if my_turtle.color() == user_bet:
                my_turtle.write("Congratulations! You WIN!", align='center')
            else:
                my_turtle.write("Alas! You LOSE!", align='center')

screen.exitonclick()