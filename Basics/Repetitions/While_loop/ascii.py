# Ask the user for input
print("\nHow many bars shall I charge?")
Chargedbars = int(input())

# Control Variable
Bars = 1

# While Loop
while (Bars <= Chargedbars):
  Bars = Bars + 1
  print("Charging:", "█" * Bars)
  
print("\nThe battery is fully charged!")