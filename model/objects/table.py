class Table:
  def __init__(self, id,name, room,tableGroup,x,y,position):
    self.id = id
    self.name = name
    self.room = room
    self.tableGroup = tableGroup
    self.x = x
    self.y = y
    self.position = position

  def getName(self):
    return self.name + " [" + self.tableGroup.getName() + "]"