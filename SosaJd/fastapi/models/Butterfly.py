from tokenize import String
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Butterfly(Base):
    __tablename__ = "butterflies"
    id = Column(Integer, primary_key=True)  # Primary key
    species = Column(String)
    color = Column(String)
    wingspan = Column(Integer)  # Wingspan in cm
    butterfly_house_id = Column(Integer, ForeignKey("butterfly_houses.id"))  # Foreign key to ButterflyHouse
    butterfly_house = relationship("ButterflyHouse", back_populates="butterflies")  # Reference back to ButterflyHouse