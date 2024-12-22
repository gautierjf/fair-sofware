
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from infrastructure.entities.base import Base

from sqlalchemy.orm import relationship

class RoomEntity(Base):
    __tablename__ = "room"
    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(50))
    x : Mapped[float]
    y : Mapped[float]
    width : Mapped[float]
    length : Mapped[float]

    def __init__(self, name, x, y,width,length):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    def __repr__(self):
        return "Room(%r)" % (self.name)
