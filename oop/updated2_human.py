class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"
  MAX_ENERGY = 100

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0
    self.energy = Robot.MAX_ENERGY
  
  # Eat
  def eat(self, amount):
    if (self.energy + amount > Robot.MAX_ENERGY):
      self.energy = Robot.MAX_ENERGY
    else:
      self.energy += amount

  # Grow
  def grow(self):
    self.age += 1

  # Move
  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
        self.energy = potential_energy
        return 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")

  # Magic method
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  print(robot.__repr__())
  robot.eat(5)
  robot.grow()
  robot.display()
  print(robot.__repr__())
  robot.grow()
  robot.display()
  print(robot.__repr__())
  robot.move(10)
  robot.grow()
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

    # Eat
  def eat(self, amount):
    if (self.energy + amount > Human.MAX_ENERGY):
      self.energy = Human.MAX_ENERGY
    else:
      self.energy += amount

    # Grow
  def grow(self):
    self.age += 1

    # Move
  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
        self.energy = potential_energy
        return 0

   # An instance method
  def display(self):
    print(f"I am {self.name}")

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old, my energy level is {self.energy}.'


if (__name__ == "__main__"):

  

  human = Human()
  human.display()
  print(human.__str__())
  human.eat(5)
  human.grow()
  human.display()
  print(human.__str__())
  human.grow()
  human.display()
  print(human.__str__())
  human.move(10)
  human.grow()
  human.display()
  print(human.__str__())