from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.db.session import get_db
from fastapi.Schemes.Butterfly_Scheme import ButterflyCreate, ButterflyResponse
from fastapi.Services.Butterfly_Service import create_butterfly, read_butterfly, read_butterflys

router = APIRouter()

@router.post("/butterfly/", status_code=201, response_model=ButterflyResponse)
def create_butterfly_route(butterfly: ButterflyCreate, db: Session = Depends(get_db)):
    return create_butterfly(db, butterfly)

@router.get("/butterfly/{butterfly_id}")
def get_butterfly_route(butterfly_id: int, db: Session = Depends(get_db)):
    return read_butterfly(db, butterfly_id)

@router.delete("/butterfly/{butterfly_id}")
def delete_butterfly(butterfly_id: int, db: Session = Depends(get_db)):
    return delete_butterfly(db, butterfly_id)

@router.get("/butterfly/")
def read_butterfly(butterfly_id: int, db: Session = Depends(get_db)):
    return read_butterflys()