
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from sqlalchemy.orm import DeclarativeBase

from infrastructure.entities.tableGroupEntity import TableGroupEntity
from infrastructure.entities.roomEntity import RoomEntity

from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.tableGroupEntity import TableGroupEntity


from infrastructure.entities.base import Base


class TableEntity(Base):
    __tablename__ = "table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    x : Mapped[float]
    y : Mapped[float]
    position: Mapped[str] = mapped_column(String(30))
    
    table_group_id: Mapped[int] = mapped_column(ForeignKey("table_group.id"))
    tableGroup: Mapped[TableGroupEntity] = relationship(
        lazy="joined"
    )
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    room: Mapped[RoomEntity] = relationship(
        lazy="joined"
    )

    def __init__(self, name, x, y,position):
        self.name = name
        self.x = x
        self.y = y
        self.position = position

    def __repr__(self):
        return "Table(%r)" % (self.name)


 