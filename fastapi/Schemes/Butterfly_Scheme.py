from pydantic import BaseModel
from typing import Optional
from Schemes.ButterflyGarden_Scheme import ButterflyGardenResponse

class ButterflyBase(BaseModel):
    species: str
    wingspan: int
    color: str
    butterfly_garden_id: Optional[int] = None

class ButterflyCreate(ButterflyBase):
    pass

class ButterflyResponse(ButterflyBase):
    id: int
    butterfly_garden: Optional[ButterflyGardenResponse] = None

    class Config:
        from_attributes = True