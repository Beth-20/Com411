def run():
  print("\nProgram Started!")
  print("\nPlease enter an Ascii code")
  code = int(input())

#Variables
  start = 32
  end = 126

# Is input in range
  if code in range (start, end):
    letter = chr(code)
    print("The character reresented by the Ascii code {} is {}".format(code,letter))
  else:
    print("The value entered is outside of the range")

# End of program
  print("Program ended!")