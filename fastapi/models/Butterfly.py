from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.ButterflyGarden import ButterflyGarden
from db.database import Base

class Butterfly(Base):
    __tablename__ = "butterflies"
    id = Column(Integer, primary_key=True)  # Primary key
    species = Column(String)
    color = Column(String)
    wingspan = Column(Integer)  # Wingspan in cm
    butterfly_garden_id = Column(Integer, ForeignKey("butterfly_garden.id"))  # Foreign key to ButterflyHouse
    butterfly_garden = relationship("ButterflyGarden", back_populates="butterflies")