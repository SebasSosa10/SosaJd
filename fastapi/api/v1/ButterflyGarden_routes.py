from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from models.ButterflyGarden import *
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate, ButterflyGardenResponse
from Services.ButterflyGarden_Service import create_butterflyGarden_serv, read_butterflyGardens_serv, read_butterflyGarden_serv,update_butterflyGarden_serv, delete_butterflyGarden_serv

router = APIRouter()

# Endpoint to create a new Butterfly Garden
# Accepts a ButterflyGardenCreate object and returns the created ButterflyGardenResponse
@router.post("/butterflyGarden/", status_code=201, response_model=ButterflyGardenResponse)
def create_butterflyGarden_route(butterflyGarden: ButterflyGardenCreate, db: Session = Depends(get_db)):
    return create_butterflyGarden_serv(butterflyGarden, db)

# Endpoint to retrieve all Butterfly Gardens
# Returns a list of ButterflyGardenResponse objects
@router.get("/butterflyGarden/", response_model=list[ButterflyGardenResponse])
def read_butterflyGardens_route(db: Session = Depends(get_db)):
    return read_butterflyGardens_serv(db)

# Endpoint to retrieve a specific Butterfly Garden by its ID
# Returns the corresponding ButterflyGarden object if found
@router.get("/butterflyGarden/{butterflyGarden_id}")
def get_butterflyGarden_route(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return read_butterflyGarden_serv(butterflyGarden_id, db)

# Endpoint to update an existing Butterfly Garden by its ID
# Accepts a ButterflyGardenCreate object with the updated data
@router.put("/butterflyGarden/{butterflyGarden_id}", response_model=ButterflyGardenResponse)
def update_butterflyGarden_route(butterflyGarden_id: int, butterflyGarden_update: ButterflyGardenCreate, db: Session = Depends(get_db)):
    return update_butterflyGarden_serv(butterflyGarden_id, butterflyGarden_update, db)

# Endpoint to delete a specific Butterfly Garden by its ID
# Returns a success message upon successful deletion
@router.delete("/butterflyGarden/{butterflyGarden_id}")
def delete_butterflyGarden_route(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return delete_butterflyGarden_serv(butterflyGarden_id, db)