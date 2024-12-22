
from model.room import Room
from model.door import Door
from model.exponent import Exponent
from model.tableGroup import TableGroup
from model.table import Table

class AppController:
  def __init__(self):
    self.rooms = []
    self.doors = []
    self.exponents = []
    self.tableGroups = []
    self.tables = []

  def addRoom(self,name,width,height):
    self.rooms.append(Room(len(self.rooms)+1,name,int(width),int(height),0,0)) 

  def getRooms(self):
    return self.rooms
  
  def addDoor(self,name,room):
    self.doors.append(Door(len(self.doors)+1,name,room,5,"Horizontal",0,0))        

  def getDoors(self):
    return self.doors
  
  def addTableGroup(self,tableWidth,tableLength,color):
    self.tableGroups.append(TableGroup(len(self.tableGroups)+1,int(tableWidth),int(tableLength),color))   

  def getTableGroups(self):
    return self.tableGroups
  
  def addTable(self,name,room,tableGroup):
    self.tables.append(Table(len(self.tables)+1,name,room,tableGroup,0,0,"Horizontal"))       

  def getTables(self):
    return self.tables

  def addExponent(self,firstName,lastName):
    self.exponents.append(Exponent(len(self.exponents)+1,firstName,lastName))       
       
  def getExponents(self):
    return self.exponents