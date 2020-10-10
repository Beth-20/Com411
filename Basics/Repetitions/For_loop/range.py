# Ask user for brightness level
print("\n What level of brightness do we need?")
brightness = int (input())

print("\n Adjusting brightness...")

# Brightness for loop
for light in range ( 2, brightness + 1, 2):
  print("\nBeeps brightness level:", "*" * light)
  print("Bops brightness level:", "*" * light)

# End
print("\nAdjustments complete! lets go!")