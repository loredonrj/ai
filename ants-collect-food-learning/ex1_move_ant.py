def move_ant():
    food_distance = 10 # Distance between ant and food
    ant_position = 0 # Ant starts at position 0
    total_steps = 0 # Number of steps taken

#loop until the ant reaches the food
    while ant_position < food_distance:
        ant_position += 1 # moves the ant forward 1 step
        total_steps += 1 # increments the step count by 1
        print(f"The ant took {total_steps} steps to reach the food. It is now at position {ant_position}.")

    print(f"Ant reached the food in {total_steps} steps.")

move_ant()