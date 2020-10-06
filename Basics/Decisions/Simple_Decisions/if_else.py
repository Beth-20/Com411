

if ("calculate" in activity): 
  print("performing calculations...")
  print("Activity completed, goodbye,")

  

  # Ask the user for the activity type
print("Please enter the activity to be performed.")
activity = input() 

# Determine if the activity is calculate
if (activity == "calculate"):
    print("\nPerforming calculations...")
else:
    print("\nPerforming activity...")

# Display message
print("\nActivity completed.")