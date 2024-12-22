class Exponent:
  def __init__(self, id,firstname, lastname):
    self.id = id
    self.firstname = firstname
    self.lastname = lastname
    
  def getName(self):
    return self.firstname + " " + self.lastname
