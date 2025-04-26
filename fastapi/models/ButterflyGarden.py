__tablename__ = "butterfly_houses"
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ButterflyHouse(Base):
    __tablename__ = "butterfly_houses"
    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String)
    location = Column(String)
    butterflies = relationship("Butterfly", back_populates="butterfly_house")  # One-to-many relationship with Butterfly
