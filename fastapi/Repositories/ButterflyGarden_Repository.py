from sqlalchemy.orm import Session
from db.session import get_db
from models.ButterflyGarden import ButterflyGarden
from fastapi import APIRouter, Depends, HTTPException
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate

# Creates a new butterfly garden in the database
def create_butterflyGarden(butterflyGarden: ButterflyGardenCreate, db:Session):
    db_ButterflyGarden = ButterflyGarden(**butterflyGarden.dict())
    db.add(db_ButterflyGarden)
    db.commit()
    db.refresh(db_ButterflyGarden)
    return db_ButterflyGarden

# Retrieves all butterfly gardens from the database
def read_butterflyGardens(db: Session = Depends(get_db)):
    butterflyGardens = db.query(ButterflyGarden).all()
    return butterflyGardens

# Retrieves a specific butterfly garden by its ID
def read_butterflyGarden(butterflyGarden_id: int, db: Session = Depends(get_db)):
    butterflyGarden = db.query(ButterflyGarden).filter(ButterflyGarden.id == butterflyGarden_id).first()
    if butterflyGarden is None:
        raise HTTPException(status_code=404, detail="ButterflyGarden not found")
    return butterflyGarden

# Updates a butterfly garden in the database by its ID
def update_butterflyGarden(butterflyGarden_id: int, butterflyGarden_update: ButterflyGardenCreate, db: Session = Depends(get_db)):
    butterflyGarden = db.query(ButterflyGarden).filter(ButterflyGarden.id == butterflyGarden_id).first()
    if butterflyGarden is None:
        raise HTTPException(status_code=404, detail="ButterflyGarden not found")
    
    for key, value in butterflyGarden_update.dict().items():
        setattr(butterflyGarden, key, value)
    
    db.commit()
    db.refresh(butterflyGarden)
    return butterflyGarden

# Deletes a butterfly garden from the database by its ID
def delete_butterflyGarden(butterflyGarden_id: int, db: Session = Depends(get_db)):
    butterflyGarden = db.query(ButterflyGarden).filter(ButterflyGarden.id == butterflyGarden_id).first()
    if butterflyGarden is None:
        raise HTTPException(status_code=404, detail="ButterflyGarden not found")
    db.delete(butterflyGarden)
    db.commit()
    return {"message": "ButterflyGarden deleted successfully"}
