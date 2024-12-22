
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from sqlalchemy.orm import Mapped
from sqlalchemy import String
from sqlalchemy.orm import mapped_column

from infrastructure.entities.base import Base

class TableGroupEntity(Base):
    __tablename__ = "table_group"
    id: Mapped[int] = mapped_column(primary_key=True)
    width : Mapped[float]
    length : Mapped[float]
    color : Mapped[str] = mapped_column(String(50))
    
    def __init__(self, width,length,color):
        self.width = width
        self.length = length
        self.color = color
