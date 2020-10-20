# Ask user for columns and rows
def run():
  print("\nHow many rows should I have?")
  rows = int(input())
  print("\n How many columns should I have?")
  columns = int(input())
  print("\nHere I go...")

# Emoji Grid
  for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()