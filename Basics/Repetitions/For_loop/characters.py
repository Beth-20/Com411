# Ask user for input
def run():
  print("\n What strange markings do you see?")
  Markings = input()

  print("\n Identifying ...")

# For loop
  for count in range (0, len(Markings), 1):
    print("\nIndex", count, ":", Markings[count])
