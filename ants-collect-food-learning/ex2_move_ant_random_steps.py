import random

def move_ant():
    food_distance = 10 # Distance between ant and food
    ant_position = 0
    step = 0

#loop until the ant reaches the food
    while ant_position < food_distance:
        step += random.randint(1,3) # sets randomly the number of steps forward (number is between 1 and 3 
        ant_position += step
        print(f"Ant took {step} step(s). It is now at position {ant_position}.")   
        if ant_position == food_distance:
            print(f"Ant reached the food in {ant_position} step(s).")
        if ant_position > food_distance:
            print(f"The ant overpassed the food by {ant_position - food_distance} step(s).")
    print(f"Ant took a total of {ant_position} steps.")

move_ant()