def run():
  import random 

# Ask for user input
  print("\nPlease enter the minimum value:")
  minimum = int(input())
  print("\nPlease enter the maximum value:")
  maximum = int(input())

  random_number = random.randrange(minimum, maximum)

  print("\nI am thinking of a number between {} and {}.".format(minimum,maximum))
  print("\nCan you guess what it is?")

  guess = 0

# If user does not guess correctly input another number
  while(guess != random_number):
    print("\nPlease enter a number:")
    guess = int(input())

# Answer message depending on user guess
  if (guess == random_number):
    print("\nCongratulations!")
  elif (guess < random_number):
    print("Guess higher")
  else:
    print("Guess lower")
  
    print("\nGame over!")