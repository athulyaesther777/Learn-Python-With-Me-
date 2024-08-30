def turn_right():
    turn_left()
    turn_left()
    turn_left()
while at_goal()==False:
    if wall_in_front():
        turn_left()
        while wall_on_right()==True:
            move()        
        turn_right()
        move()
        turn_right()
        while front_is_clear():
              move()
        turn_left()                   
    else:
        move()
