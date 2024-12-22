class Door:
  def __init__(self, id,name,room, width,position,x,y):
    self.id = id
    self.name = name
    self.room = room
    self.width = width
    self.position = position
    self.x = x
    self.y = y

  def getName(self):
    return self.name + " [" + self.room.name + "]"
