class Room:
  def __init__(self, id,name, width,length,x,y):
    self.id = id
    self.name = name
    self.width = int(width)
    self.length = int(length)
    self.x = x
    self.y = y

  def getName(self):
    return self.name
