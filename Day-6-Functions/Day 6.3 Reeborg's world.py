def move():
    pass


def turn_left():
    pass


def turn_around():
    turn_left()
    turn_left()
    turn_left()


def looped_move():
    move()
    turn_left()
    turn_around()
    move()
    turn_around()
    move()


looped_move()
