# Ask user for input
def run():
  print("\n How many mountains shall I display?")
  mountains = int(input())

# Mountains
  print("\nDisplaying...")

  for mountain in range(mountains):
    print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\


     """)