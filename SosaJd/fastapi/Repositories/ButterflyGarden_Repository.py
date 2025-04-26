from sqlalchemy.orm import Session
from models.ButterflyGarden import ButterflyGarden
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate


def create_ButterflyGarden(db: Session, butterflyGarden: ButterflyGardenCreate):
    db_ButterflyGarden = ButterflyGarden(**butterflyGarden.dict())
    db.add(db_ButterflyGarden)
    db.commit()
    db.refresh(db_ButterflyGarden)
    return db_ButterflyGarden

def get_ButterflyGarden(db: Session, butterflyGarden_id: int):
    return db.query(ButterflyGarden).filter(ButterflyGarden.id == butterflyGarden_id).first()