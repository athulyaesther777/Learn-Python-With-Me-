def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear() and not front_is_clear():  # Only turn right if it can't move forward
        turn_right()
        move()
    elif front_is_clear():  # Move forward if possible
        move()
    else:  # Otherwise, turn left
        turn_left()
