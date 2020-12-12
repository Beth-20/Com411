
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

  # Magic Method
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old, my energy level is {self.energy}.'


if (__name__ == "__main__"):
  human = Human()
  human.display()
  print(human.__str__())
