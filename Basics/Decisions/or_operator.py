# Ask user for journey type
def run():
  print("\nHello its me Beep and I need help with my adventure")
  print("\nWhat type of adventure should I have? Scary, Safe, Long or Short?")
  Adventuretype = input()

# Scary / Short Adventure
  if ((Adventuretype.lower == "scary") or (Adventuretype.lower == "short")):
    print("Entering the dark forest!...")

# Safe / Long Adventure
  elif ((Adventuretype.lower == "safe") or (Adventuretype.lower == "long")):
    print("Taking the safe route!")
  else:
    print("Oh No! I'm not sure which route to take!")