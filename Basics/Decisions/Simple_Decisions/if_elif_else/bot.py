# Ask user for the direction 
print("Which direction should I paint human (up, down, left or right)?")
direction = input() 

# Determine which direction to display
if (direction == "up"):
    print("\nThank you, I am going to paint in the upward direction!")
elif (direction == "down"):
    print("\nThank you, I am going to paint in the downward direction!")
elif (direction == "left"):
    print("\nThank you, I am going to paint in the leftward direction!")
elif (direction == "right"):
    print("\nThank you, I am going to paint in the rightward direction!")
else:
    print("\nOh No I'm not sure which direction in am supposed to be painting in!")