# Define the function
def cross_bridge(steps):

  for step in range (steps):
    print("Crossed step")
  if (steps > 5):
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")

# Call the function
cross_bridge(3)
cross_bridge(6)
