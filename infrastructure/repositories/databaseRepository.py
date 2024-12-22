
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


from infrastructure.entities.tableEntity import TableEntity
from infrastructure.entities.tableGroupEntity import TableGroupEntity
from infrastructure.entities.roomEntity import RoomEntity


from model.objects.table import Table
from model.objects.tableGroup import TableGroup
from model.objects.room import Room

from infrastructure.entities.base import Base

class DatabaseRepository:
  def __init__(self):
    engine = create_engine("sqlite:///gestionfoire.db")
    Base.metadata.create_all(engine)
    self.session = Session(engine)

  def getTables(self):
    tableEntities = self.session.query(TableEntity).join(TableGroupEntity).join(RoomEntity).all()
    tables = []
    for i in range(0,len(tableEntities),1):
      tableEntity = tableEntities[i]
      tableGroupEntity = tableEntity.tableGroup
      roomEntity = tableEntity.room
      tableGroup = TableGroup(tableGroupEntity.id,tableGroupEntity.width,tableGroupEntity.length,tableGroupEntity.color)
      room = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
      table = Table(tableEntity.id,tableEntity.name,room,tableGroup,tableEntity.x,tableEntity.y,tableEntity.position)
      tables.append(table)
    return tables

  def addTable(self,table):
    tableEntity = TableEntity(table.name,table.x,table.y,table.position)
    tableGroupEntity = self.session.query(TableGroupEntity).filter_by(id=table.tableGroup.id).one()
    tableEntity.tableGroup = tableGroupEntity
    roomEntity = self.session.query(RoomEntity).filter_by(id=table.room.id).one()
    tableEntity.room = roomEntity
    self.session.add(tableEntity)
    self.session.commit()

  def updateTable(self,table):
    self.session.query(TableEntity).filter_by(id=table.id).update({"x":table.x,"y":table.y})
    self.session.commit()


  def addTableGroup(self,tableGroup):
    tableGroupEntity = TableGroupEntity(tableGroup.width,tableGroup.length,tableGroup.color)
    self.session.add(tableGroupEntity)
    self.session.commit()

  def getTableGroups(self):
    tableGroupEntities = self.session.query(TableGroupEntity).all()
    tableGroups = []
    for i in range(0,len(tableGroupEntities),1):
      tableGroupEntity = tableGroupEntities[i]
      tableGroup = TableGroup(tableGroupEntity.id,tableGroupEntity.width,tableGroupEntity.length,tableGroupEntity.color)
      tableGroups.append(tableGroup)
    return tableGroups

  def addRoom(self,room):
    roomEntity = RoomEntity(room.name,room.x,room.y,room.width,room.length)
    self.session.add(roomEntity)
    self.session.commit()

  def getRooms(self):
    roomEntities = self.session.query(RoomEntity).all()
    rooms = []
    for i in range(0,len(roomEntities),1):
      roomEntity = roomEntities[i]
      room = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
      rooms.append(room)
    return rooms