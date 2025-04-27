from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class ButterflyGarden(Base):
    __tablename__ = "butterfly_garden"
    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String)
    location = Column(String)
    butterflies = relationship("Butterfly", back_populates="butterfly_garden")  # One-to-many relationship with Butterfly
