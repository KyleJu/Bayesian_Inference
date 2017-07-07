import random as ra
class simulation():
  def __init__(self, p, size):
    self.p = p
    self.size = size

  def simulate_conversion(self):
    res = [ra.random() < self.p for i in range(self.size)]
    return sum(res)
  


