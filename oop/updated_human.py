class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  print(robot.__repr__())

class Human:

  #Class Attribute
  MAX_ENERGY = 100

  #Instance attributes

  def __init__(self):

    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

   # An instance method
  def display(self):
    print(f"I am {self.name}")

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old, my energy level is {self.energy}.'


if (__name__ == "__main__"):
  human = Human()
  human.display()
  print(human.__str__())
