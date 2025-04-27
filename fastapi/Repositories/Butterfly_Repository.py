from sqlalchemy.orm import Session
from db.session import get_db
from models.Butterfly import Butterfly
from fastapi import APIRouter, Depends, HTTPException
from Schemes.Butterfly_Scheme import ButterflyCreate

def create_butterfly(butterfly: ButterflyCreate, db: Session):
    db_Butterfly = Butterfly(**butterfly.dict())
    db.add(db_Butterfly)
    db.commit()
    db.refresh(db_Butterfly)
    return db_Butterfly

def read_butterflies(db: Session = Depends(get_db)):
    butterflies = db.query(Butterfly).all()
    return butterflies

def read_butterfly(butterfly_id: int, db: Session = Depends(get_db)):
    butterfly = db.query(Butterfly).filter(Butterfly.id == butterfly_id).first()
    if butterfly is None:
        raise HTTPException(status_code=404, detail="Butterfly not found")
    return butterfly

def delete_butterfly(butterfly_id: int, db: Session = Depends(get_db)):
    butterfly = db.query(Butterfly).filter(Butterfly.id == butterfly_id).first()
    if butterfly is None:
        raise HTTPException(status_code=404, detail="Butterfly not found")
    db.delete(butterfly)
    db.commit()
    return {"message": "Butterfly deleted successfully"}

def update_butterfly(butterfly_id: int, butterfly_update: ButterflyCreate, db: Session = Depends(get_db)):
    butterfly = db.query(Butterfly).filter(Butterfly.id == butterfly_id).first()
    if butterfly is None:
        raise HTTPException(status_code=404, detail="Butterfly not found")
    
    for key, value in butterfly_update.dict(exclude_unset=True).items():
        setattr(butterfly, key, value)
    
    db.commit()
    db.refresh(butterfly)
    return butterfly