# function 1 
def search (filepath):
  print("Searching...")

  with open(filepath) as file:
    for line in file: 
      print(f"Looked in {line}")

    print("... Done!")
  


# function 2 
def run (): 
  location = search("Data/Files/txt/locations.txt")

# call the function
run ()