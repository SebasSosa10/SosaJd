from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from models.ButterflyGarden import *
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate, ButterflyGardenResponse
from Services.ButterflyGarden_Service import create_butterflyGarden, read_butterflyGarden, read_butterflyGardens

router = APIRouter()

@router.post("/butterflyGarden/", status_code=201, response_model=ButterflyGardenResponse)
def create_butterflyGarden_route(butterflyGarden: ButterflyGardenCreate, db: Session = Depends(get_db)):
    return create_butterflyGarden(db, butterflyGarden)

@router.get("/butterflyGarden/{butterflyGarden_id}")
def get_butterflyGarden_route(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return read_butterflyGarden(db, butterflyGarden_id)

@router.delete("/butterflyGarden/{butterflyGarden_id}")
def delete_butterflyGarden(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return delete_butterflyGarden(db, butterflyGarden_id)

@router.get("/butterflyGarden/")
def read_butterflyGarden(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return read_butterflyGardens()