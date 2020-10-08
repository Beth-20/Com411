# Ask for user input
print("\nHow many live cables shall I avoid?")
Avoidcables = int(input())

# Control Variable
Livecables = 0

# While loop
while (Livecables < Avoidcables):
  print("Avoiding...", end="")
  Livecables = Livecables +1
  print("Done!", Livecables, "Cables Avoided")

print("All live cables avoided!")