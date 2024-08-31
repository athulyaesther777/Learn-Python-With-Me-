def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():  # Continue until Reeborg reaches the goal
    if right_is_clear():  # Check if Reeborg can turn right
        turn_right()      # If yes, turn right
        move()            # Then move forward
    elif front_is_clear():  # If right is blocked, check if the front is clear
        move()              # If yes, move forward
    else:
        turn_left()  # If both right and front are blocked, turn left
