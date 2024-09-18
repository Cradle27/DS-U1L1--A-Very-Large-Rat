class Rat:
  def __init__(self, sex, weight):
    self.sex = sex
    self.weight = weight
    self.litters = 0

  def __str__(self):
    return f"{self.sex} {self.weight}"

  def repr(self):
    return repr(f"{self.sex} {self.weight}")

  def getWeight(self):
    return self.weight

  def getSex(self):
    return self.sex

  def canBreed(self):
    if self.litters >= 5:
      return False
    else:
      return True


  def __lt__(self, other):
    return self.litters < other

  def __le__(self, other):
    return self.litters <= other

  def __gt__(self, other):
    return self.litters > other

  def __ge__(self, other):
    return self.litters >= other

  def __eq__(self, other):
    return self.litters == other

  


