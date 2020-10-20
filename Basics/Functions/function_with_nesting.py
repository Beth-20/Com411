def run():
# Define see function
  def identify():
  # Ask user for what they can see
    print("\nWhat can you see up ahead?")
    ahead = input()

    if (ahead.lower() == "a large boulder"):
      print("Its time to run!")
    else:
      print("We will be fine")

    
# Call to function
  identify()