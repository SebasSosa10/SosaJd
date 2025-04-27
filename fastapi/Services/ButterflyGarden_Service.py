from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from db.session import get_db   
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate
from Repositories.ButterflyGarden_Repository import create_butterflyGarden, read_butterflyGarden, read_butterflyGardens, delete_butterflyGarden

def create_butterflyGarden_serv(butterflyGarden: ButterflyGardenCreate, db: Session = Depends(get_db)):
    return create_butterflyGarden(butterflyGarden, db)

def read_butterflyGarden_serv(butterfly_garden_id: int, db: Session = Depends(get_db)):
    return read_butterflyGarden(butterfly_garden_id, db)

def read_butterflyGardens_serv(db: Session):
    return read_butterflyGardens(db)

def delete_butterflyGarden_serv(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return delete_butterflyGarden(butterflyGarden_id, db)