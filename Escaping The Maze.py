#Designed for Reeborg
# URL Link
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
            
while not at_goal():
    while not wall_on_right():
        turn_right()
        move()        
    if wall_in_front() == False:
        move()
    elif wall_in_front() == True:        
        if right_is_clear() == True:
            turn_right()
            move()
        elif wall_on_right() == True:
            turn_left()           
            if front_is_clear() == True:
                move()
            elif wall_on_right() == True:
                turn_left()
                move()
'''