from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from models.ButterflyGarden import *
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate, ButterflyGardenResponse
from Services.ButterflyGarden_Service import create_butterflyGarden_serv, read_butterflyGarden_serv, delete_butterflyGarden_serv, read_butterflyGardens_serv

router = APIRouter()

@router.post("/butterflyGarden/", status_code=201, response_model=ButterflyGardenResponse)
def create_butterflyGarden_route(butterflyGarden: ButterflyGardenCreate, db: Session = Depends(get_db)):
    return create_butterflyGarden_serv(butterflyGarden, db)

@router.get("/butterflyGarden/{butterflyGarden_id}")
def get_butterflyGarden_route(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return read_butterflyGarden_serv(butterflyGarden_id, db)

@router.get("/butterflyGarden/")
def read_butterflyGarden_route(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return read_butterflyGardens_serv(db)

@router.delete("/butterflyGarden/{butterflyGarden_id}")
def delete_butterflyGarden_route(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return delete_butterflyGarden_serv(butterflyGarden_id, db)