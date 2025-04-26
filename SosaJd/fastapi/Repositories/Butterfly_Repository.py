from sqlalchemy.orm import Session
from models.Butterfly import Butterfly
from Schemes.Butterfly_Scheme import ButterflyCreate


def create_Butterfly(db: Session, butterfly: ButterflyCreate):
    db_Butterfly = Butterfly(**butterfly.dict())
    db.add(db_Butterfly)
    db.commit()
    db.refresh(db_Butterfly)
    return db_Butterfly

def get_Butterfly(db: Session, butterfly_id: int):
    return db.query(Butterfly).filter(Butterfly.id == butterfly_id).first()