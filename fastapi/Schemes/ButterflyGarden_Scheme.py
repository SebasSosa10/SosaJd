from pydantic import BaseModel

class ButterflyGardenBase(BaseModel):
    name: str
    location: str

class ButterflyGardenCreate(ButterflyGardenBase):
    pass

class ButterflyGardenResponse(ButterflyGardenBase):
    id: int
    class Config:
        orm_mode = True