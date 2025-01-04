
from model.objects.room import Room
from model.objects.door import Door
from model.objects.exponent import Exponent
from model.objects.tableGroup import TableGroup
from model.objects.table import Table
from model.usecases.computeUsecase import ComputeUsecase

from infrastructure.repositories.databaseRepository import DatabaseRepository

import csv

class AppController:
  def __init__(self,window,databaseRepository):
    self.rooms = []
    self.doors = []
    self.exponents = []
    self.tableGroups = []
    self.tables = []
    self.window = window
    self.databaseRepository = databaseRepository

  def addRoom(self,name,width,height):
    room = Room(len(self.rooms)+1,name,int(width),int(height),0,0)
    self.databaseRepository.addRoom(room)
    self.rooms.append(room)   
    self.window.displayDrawer("controller")

  def loadModel(self):
    self.tables = self.databaseRepository.getTables()
    self.rooms = self.databaseRepository.getRooms()
    self.tableGroups = self.databaseRepository.getTableGroups()
    self.exponents = self.databaseRepository.getExponents()
  
  def getRooms(self):
    return self.rooms
  
  def addDoor(self,name,room):
    self.doors.append(Door(len(self.doors)+1,name,room,5,"Horizontal",0,0))     
    self.window.displayDrawer("controller")

  def getDoors(self):
    return self.doors
  
  def addTableGroup(self,tableWidth,tableLength,color):
    tableGroup = TableGroup(len(self.tableGroups)+1,int(tableWidth),int(tableLength),color)
    self.databaseRepository.addTableGroup(tableGroup)
    self.tableGroups.append(tableGroup)   
    self.window.displayDrawer("controller")

  def getTableGroups(self):
    return self.tableGroups
  
  def addTable(self,name,room,tableGroup,position):
    table = Table(len(self.tables)+1,name,room,tableGroup,10,10,position)
    self.databaseRepository.addTable(table)
    self.tables.append(table)       
    self.window.displayDrawer("controller")
    
  def updatePositionTable(self,index,x,y):
    table = self.tables[index];
    table.x = x
    table.y = y
    self.databaseRepository.updateTable(table)

  def getTables(self):
    return self.tables

  def addExponent(self,firstName,lastName):
    exponent = Exponent(len(self.exponents)+1,firstName,lastName)
    self.exponents.append(Exponent(len(self.exponents)+1,firstName,lastName))  
    self.databaseRepository.addExponent(exponent)  
    self.window.displayDrawer("controller")
       
  def getExponents(self):
    return self.exponents
  
         
  def importExponents(self,filename):
    importedExponents = []
    with open(filename,'r',encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                importedExponents.append(Exponent(len(importedExponents)+1,row[3],row[4]))
                print(f'\t{row[3]} {row[4]} ')
                line_count += 1
        print(f'Processed {line_count} lines.')
    csv_file.close()
    for exponent in importedExponents:
      self.databaseRepository.addExponent(exponent)  
      self.exponents.append(exponent)
    
  def fillRoom(self,room,tableGroup,distanceFromTheWall,numberOfAlleys,widthAlley):
    usecase = ComputeUsecase(room,tableGroup,int(distanceFromTheWall),int(numberOfAlleys),int(widthAlley))
    tables = usecase.execute()
    self.tables = tables    
    self.window.displayDrawer("controller")

  def goBack(self):
    self.window.displayDrawer("controller")