# funtion 1
def observed():
  observations = []

# user input for loop (7)
  for count in range(7):
    print("Please enter an observation")
    observation = input()
    observations.append(observation)

  return observations 

# function 2 
def run():
  print("Counting observations...")
  observations = observed()
  observations_set = set()
  for observation in observations:
    observations_set.add((observation, observations.count(observation)))

  print(observations_set)

run()