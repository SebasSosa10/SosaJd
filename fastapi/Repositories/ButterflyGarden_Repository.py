from sqlalchemy.orm import Session
from db.session import get_db
from models.ButterflyGarden import ButterflyGarden
from fastapi import APIRouter, Depends, HTTPException
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate


def create_butterflyGarden(butterflyGarden: ButterflyGardenCreate, db:Session):
    db_ButterflyGarden = ButterflyGarden(**butterflyGarden.dict())
    db.add(db_ButterflyGarden)
    db.commit()
    db.refresh(db_ButterflyGarden)
    return db_ButterflyGarden

def read_butterflyGarden(butterflyGarden_id: int, db: Session = Depends(get_db)):
    butterflyGarden = db.query(ButterflyGarden).filter(ButterflyGarden.id == butterflyGarden_id).first()
    if butterflyGarden is None:
        raise HTTPException(status_code=404, detail="ButterflyGarden not found")
    return butterflyGarden

def read_butterflyGardens(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    butterflyGarden = db.query(ButterflyGarden).offset(skip).limit(limit).all()
    return butterflyGarden

def delete_butterflyGarden(butterflyGarden_id: int, db: Session = Depends(get_db)):
    butterflyGarden = db.query(ButterflyGarden).filter(ButterflyGarden.id == butterflyGarden_id).first()
    if butterflyGarden is None:
        raise HTTPException(status_code=404, detail="ButterflyGarden not found")
    db.delete(butterflyGarden)
    db.commit()
    return {"message": "ButterflyGarden deleted successfully"}
