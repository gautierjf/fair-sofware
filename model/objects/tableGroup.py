class TableGroup:
  def __init__(self, id,width, length,color):
    self.id = id
    self.width = int(width)
    self.length = int(length)
    self.color = color

  def getName(self):
    return str(self.width) + " x " + str(self.length)
