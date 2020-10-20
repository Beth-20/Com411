# Ask the user how many cables to remove
def run():
  print("\nHello its me Beep! I need help rescuing another robot!")
  print("How many cables shall I remove?")
  Cables = int(input())

# Variable
  Removedcables = 0

# While loop
  while ( Removedcables < Cables):
    print("Removed Cables")
    Removedcables = Removedcables +1 
