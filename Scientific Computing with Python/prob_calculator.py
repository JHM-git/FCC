import copy
import random

class Hat:
  def __init__(self, **balls):
    self.contents = []
    for key, value in balls.items():
      count = value
      while count > 0:
        self.contents.append(key)
        count = count - 1
    
  def draw(self, num, pop=True):
    if num > len(self.contents):
      num = len(self.contents)
    drawn = random.sample(self.contents, num)
    if pop == True:
      for item in drawn:
        self.contents.pop(self.contents.index(item))
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected_list = []
  for key, value in expected_balls.items():
    count = value
    while count > 0:
      expected_list.append(key)
      count = count - 1
  M = 0
  drawn = []
  expected_copy = expected_list.copy()
  for i in range(num_experiments):
    drawn = hat.draw(num_balls_drawn, pop=False)
    for item in drawn:
      try:
        expected_copy.index(item)
        expected_copy.remove(item)
      except:
        continue
    if len(expected_copy) == 0:
      M = M + 1
    expected_copy = expected_list.copy()
  probability = M / num_experiments
  return probability
  

