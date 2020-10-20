# Ask user for number
def run():
  print("\nHow many numbers should I sum up?")
  Input1 = int(input())

# Variables
  summed = 1
  total = 0

# While loop
  while (summed <= Input1):
    print("\nPlease enter number", summed, "of", Input1, ":")
    number = int(input())
    total = total + number
    summed = summed + 1


  print("The answer is", total)