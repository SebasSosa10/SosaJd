from sqlalchemy.orm import Session
from models.ButterflyGarden import ButterflyGarden
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate

def read_butterflyGardens(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    butterflyGarden = db.query(ButterflyGarden).offset(skip).limit(limit).all()
    return butterflyGarden

def create_butterflyGarden(name: str, description: str = None, db: Session = Depends(get_db)):
    butterflyGarden = ButterflyGarden(name=name, description=description)
    db.add(butterflyGarden)
    db.commit()
    db.refresh(butterflyGarden)
    return butterflyGarden

def read_butterflyGarden(butterflyGarden_id: int, db: Session = Depends(get_db)):
    butterflyGarden = db.query(ButterflyGarden).filter(ButterflyGarden.id == butterflyGarden_id).first()
    if butterflyGarden is None:
        raise HTTPException(status_code=404, detail="ButterflyGarden not found")
    return butterflyGarden

def delete_butterflyGarden(butterflyGarden_id: int, db: Session = Depends(get_db)):
    butterflyGarden = db.query(ButterflyGarden).filter(ButterflyGarden.id == butterflyGarden_id).first()
    if butterflyGarden is None:
        raise HTTPException(status_code=404, detail="ButterflyGarden not found")
    db.delete(butterflyGarden)
    db.commit()
    return {"message": "ButterflyGarden deleted successfully"}