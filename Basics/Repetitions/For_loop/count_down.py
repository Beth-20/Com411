# Ask user for steps
print("\n How many steps away from the cave are we?")
Steps = int(input())

# For loop
for count in range ( Steps, 0, -1): 
  print( count , "steps remaining...")

print("\nHooray we have reached the cave!")
