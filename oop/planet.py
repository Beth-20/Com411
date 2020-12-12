from final_human import Human 
from final_robot import Robot
from inhabitant import Inhabitant

class Planet(Inhabitant):

  def __init__(self):
    self.inhabitants = []
     
  def __repr__(self):
    return f"planet(inhabitants={self.inhabitants})"

  def __str__(self):
    return f"This planet has {len(self.inhabitants)} inhabitants."

  def add(self, inhabitant):
    self.inhabitants.append(inhabitant)


  def remove(self, inhabitant):
    self.inhabitants.remove(inhabitant)


if (__name__ == "__main__"):
  planet = Planet()
  print(repr(planet))
  beth = Human("Beth")
  planet.add(beth)
  print(repr(planet))
  print(planet)
