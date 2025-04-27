from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from models.Butterfly import *
from Schemes.Butterfly_Scheme import ButterflyCreate, ButterflyResponse
from Services.Butterfly_Service import create_butterfly_serv, read_butterfly_serv, read_butterflys_serv, delete_butterfly_serv

router = APIRouter()

@router.post("/butterfly/", status_code=201, response_model=ButterflyResponse)
def create_butterfly_route(butterfly: ButterflyCreate, db: Session = Depends(get_db)):
    return create_butterfly_serv(butterfly, db)

@router.get("/butterfly/{butterfly_id}")
def get_butterfly_route(butterfly_id: int, db: Session = Depends(get_db)):
    return read_butterfly_serv(butterfly_id, db)

@router.delete("/butterfly/{butterfly_id}")
def delete_butterfly_route(butterfly_id: int, db: Session = Depends(get_db)):
    return delete_butterfly_serv(butterfly_id, db)

@router.get("/butterfly/")
def read_butterflys_route(butterfly_id: int, db: Session = Depends(get_db)):
    return read_butterflys_serv(db)