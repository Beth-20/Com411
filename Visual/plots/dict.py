import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}
  print("What type of line would you like? :, -- or -")
  line = input()
  print("What colour line would you like? r, g or b")
  colour = input()
  print("What marker style would you like? o, s or ^")
  marker = input()

  paths['line'] = line
  paths['colour'] = colour
  paths['marker'] = marker

  return paths

def generate():
  print("How many lines would you like to display?")
  num_lines = int(input())
  
  for num_line in range(num_lines):
    values = data()
    x = rnd.sample(range(1, 10), 5)
    y = rnd.sample(range(1, 10), 5)
    format = f"{values['colour']}{values['line']}{values['marker']}"
    plt.plot(x, y, format)
  
  plt.show()


def run():
  print("Running...")
  generate()
  print("Done!")

run()