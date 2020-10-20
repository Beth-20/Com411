# Define movement function with no parameters
def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

# Define run function with no parameters
def run():
  print("Moving...")
  path = movements()
  print("{} for {} steps".format(path[0], path[1]))
  print("{} for {} steps".format(path[2], path[3]))
  print("{} for {} steps".format(path[4], path[5]))
  print("{} for {} steps".format(path[6], path[7]))

run()