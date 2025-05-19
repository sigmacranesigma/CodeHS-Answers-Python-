
#Make Karel turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Make a tower
def tower():
    move()
    put_ball()
    turn_left()
    move()
    put_ball()
    move()
    put_ball()
    turn_right()
    turn_right()
    move()
    move()
    turn_left()
    move()
#Move and make towers
tower()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
turn_right()