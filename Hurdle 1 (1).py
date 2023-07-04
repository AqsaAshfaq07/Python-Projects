def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def square():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for jump in range(0, 6):
    square()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
