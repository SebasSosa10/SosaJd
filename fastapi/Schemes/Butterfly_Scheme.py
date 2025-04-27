from pydantic import BaseModel

class ButterflyBase(BaseModel):
    species: str
    wingspan: int
    color: str

class ButterflyCreate(ButterflyBase):
    pass


class ButterflyResponse(ButterflyBase):
    id: int
    class Config:
        orm_mode = True