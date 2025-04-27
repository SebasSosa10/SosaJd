from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from db.session import get_db   
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate
from Repositories.ButterflyGarden_Repository import create_butterflyGarden, read_butterflyGarden, read_butterflyGardens, delete_butterflyGarden

def read_butterflyGardens(db: Session):
    return read_butterflyGardens(db)

def read_butterflyGarden(butterfly_garden_id: int, db: Session = Depends(get_db)):
    return read_butterflyGarden(butterfly_garden_id, db)

def create_butterflyGarden(butterflyGarden: ButterflyGardenCreate, db: Session = Depends(get_db)):
    return create_butterflyGarden(butterflyGarden, db)

def delete_butterflyGarden(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return delete_butterflyGarden(butterflyGarden_id, db)