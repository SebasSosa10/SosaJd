from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from db.session import get_db   
from Schemes.ButterflyGarden_Scheme import ButterflyGardenCreate
from Repositories.ButterflyGarden_Repository import create_butterflyGarden, read_butterflyGarden, read_butterflyGardens,update_butterflyGarden, delete_butterflyGarden

# Service function to create a butterfly garden
# It calls the create_butterflyGarden function with the garden data and the database session
def create_butterflyGarden_serv(butterflyGarden: ButterflyGardenCreate, db: Session = Depends(get_db)):
    return create_butterflyGarden(butterflyGarden, db)

# Service function to retrieve all butterfly gardens
# It calls the read_butterflyGardens function with the database session
def read_butterflyGardens_serv(db: Session = Depends(get_db)):
    return read_butterflyGardens(db)

# Service function to retrieve a specific butterfly garden by its ID
# It calls the read_butterflyGarden function with the garden ID and the database session
def read_butterflyGarden_serv(butterfly_garden_id: int, db: Session = Depends(get_db)):
    return read_butterflyGarden(butterfly_garden_id, db)

# Service function to update a butterfly garden by its ID
# It calls the update_butterflyGarden function with the garden ID, updated data, and the database session
def update_butterflyGarden_serv(butterflyGarden_id: int, butterflyGarden_update: ButterflyGardenCreate, db: Session = Depends(get_db)):
    return update_butterflyGarden(butterflyGarden_id, butterflyGarden_update, db)

# Service function to delete a butterfly garden by its ID
# It calls the delete_butterflyGarden function with the garden ID and the database session
def delete_butterflyGarden_serv(butterflyGarden_id: int, db: Session = Depends(get_db)):
    return delete_butterflyGarden(butterflyGarden_id, db)
