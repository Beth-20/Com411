# function 1
def cwd (): 
  import os
  path = os.getcwd()
  print(f"Current Working Folder Path: {path}")
  print ("The folder contains the following:")
  for file in os.listdir(path):
    print(file)



# function 2
def run ():
  print ("Processing...")
  cwd ()

run()