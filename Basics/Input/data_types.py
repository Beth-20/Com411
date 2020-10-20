# Read in user's name
def run():
  print("What is your name human?")
  name = input()
  print("How old are you (in years)?")
  Age = float(input())
  print("How tall are you (in meters)?")
  Height = float(input())
  print("How much do you weigh (in kilograms)?")
  Weight = float(input())
  bmi = Weight / (Height*Height)
  formattedbmi = format(bmi, ".2f")
  print("You are",Age,"years old and your bmi is",formattedbmi,)