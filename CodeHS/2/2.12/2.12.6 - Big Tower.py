# This program draws a big tower from Karel's starting spot
if facing_south():
    turn_around()

if facing_west():
    turn_right()

if facing_east():
    turn_left()

while no_balls_present():
    put_ball()
    if front_is_clear():
        move()