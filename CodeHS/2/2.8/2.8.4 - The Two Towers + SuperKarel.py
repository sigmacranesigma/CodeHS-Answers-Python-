# This has karel build two towers, with three balls in each tower.
# Should be the same program with turn_right and turn_around removed.
def line():
    put_ball()
    move()
    move()
    put_ball()

move()
line()
turn_left()
move()
turn_left()
line()
turn_right()
move()
turn_right()
line()
turn_left()
move()
turn_right()