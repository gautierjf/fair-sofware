
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from infrastructure.entities.base import Base

from sqlalchemy.orm import relationship

class ExponentEntity(Base):
    __tablename__ = "exponent"
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname : Mapped[str] = mapped_column(String(50))
    lastname : Mapped[str] = mapped_column(String(50))

    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return "Exponent(%r)" %  (self.lastname)
