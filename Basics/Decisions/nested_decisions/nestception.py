# Ask user for location 
def run():
  print("\nHello its me Beep and I need help finding my battery")
  print("\nWhere shall I look? In the bedroom, bathroom or lab?")
  room = input()

# Bedroom
  if (room.lower() == "in the bedroom"):
    print("Where in the bedroom should I look?")
    bedroom = input()

    if (bedroom.lower() == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

# Bathroom
  elif (room.lower() == "in the bathroom"):
    print("Where in the bathroom shall I look?")
    bathroom = input()

    if (bathroom.lower() == "In the bath tub"):
        print("Found a rubber ducky but no battery")
    else:
       print("Found a wet surface but no battery")

# Lab
  elif (room.lower() == "in the lab"):
    print("Where in the lab shall I look?")
    lab_place = input()

    if (lab_place.lower() == "on the table"):
      print("Hooray! I found my battery!")
    else:
       print("Found some tools but no battery")
    