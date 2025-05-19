def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def move_twice():
    move()
    move()

def bury_ball():
    move_twice()
    turn_right()
    move_twice()
    move()
    put_ball()
    turn_left()
    turn_left()
    move_twice()
    move()
    turn_right()
    move()

bury_ball()
bury_ball()
bury_ball()