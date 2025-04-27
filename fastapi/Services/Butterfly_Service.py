from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from db.session import get_db   
from Schemes.Butterfly_Scheme import ButterflyCreate
from Repositories.Butterfly_Repository import read_butterfly, read_butterflys, delete_butterfly, create_butterfly

def read_butterflys_serv(db: Session):
    return read_butterflys(db)

def read_butterfly_serv(butterfly_id: int, db: Session = Depends(get_db)):
    return read_butterfly(butterfly_id, db)

def create_butterfly_serv(butterfly: ButterflyCreate, db: Session = Depends(get_db)):
    return create_butterfly(butterfly, db)

def delete_butterfly_serv(butterfly_id: int, db: Session = Depends(get_db)):
    return delete_butterfly(butterfly_id, db)