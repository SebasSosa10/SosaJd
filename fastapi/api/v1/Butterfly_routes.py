from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from models.Butterfly import *
from Schemes.Butterfly_Scheme import ButterflyCreate, ButterflyResponse
from Services.Butterfly_Service import create_butterfly_serv, read_butterfly_serv, read_butterflies_serv, delete_butterfly_serv, update_butterfly_serv

router = APIRouter()

# Endpoint to create a new butterfly
# Accepts a ButterflyCreate object and returns a ButterflyResponse with the created butterfly
@router.post("/butterfly/", status_code=201, response_model=ButterflyResponse)
def create_butterfly_route(butterfly: ButterflyCreate, db: Session = Depends(get_db)):
    return create_butterfly_serv(butterfly, db)

# Endpoint to get a specific butterfly by its ID
# Returns the butterfly matching the provided ID
@router.get("/butterfly/{butterfly_id}")
def get_butterfly_route(butterfly_id: int, db: Session = Depends(get_db)):
    return read_butterfly_serv(butterfly_id, db)

# Endpoint to delete a butterfly by its ID
# Returns a success message once the butterfly is deleted
@router.delete("/butterfly/{butterfly_id}")
def delete_butterfly_route(butterfly_id: int, db: Session = Depends(get_db)):
    return delete_butterfly_serv(butterfly_id, db)

# Endpoint to get a list of all butterflies
# Returns a list of butterflies
@router.get("/butterfly/")
def read_butterflies_route(db: Session = Depends(get_db)):
    return read_butterflies_serv(db)

# Endpoint to update a butterfly's information by its ID
# Accepts a ButterflyCreate object with the updated data
@router.put("/butterfly/{butterfly_id}")
def update_butterfly_route(butterfly_id: int, butterfly_update: ButterflyCreate, db: Session = Depends(get_db)):
    return update_butterfly_serv(butterfly_id, butterfly_update, db)