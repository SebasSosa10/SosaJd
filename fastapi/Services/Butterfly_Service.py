from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from db.session import get_db   
from Schemes.Butterfly_Scheme import ButterflyCreate
from Repositories.Butterfly_Repository import read_butterfly, read_butterflies, delete_butterfly, create_butterfly, update_butterfly

# Service function to get a list of all butterflies
# It calls the read_butterflies function with the database session
def read_butterflies_serv(db: Session = Depends(get_db)):
    return read_butterflies(db)

# Service function to get a specific butterfly by its ID
# It calls the read_butterfly function with the butterfly ID and database session
def read_butterfly_serv(butterfly_id: int, db: Session = Depends(get_db)):
    return read_butterfly(butterfly_id, db)

# Service function to create a new butterfly
# It calls the create_butterfly function with the butterfly data and the database session
def create_butterfly_serv(butterfly: ButterflyCreate, db: Session = Depends(get_db)):
    return create_butterfly(butterfly, db)

# Service function to delete a butterfly by its ID
# It calls the delete_butterfly function with the butterfly ID and database session
def delete_butterfly_serv(butterfly_id: int, db: Session = Depends(get_db)):
    return delete_butterfly(butterfly_id, db)

# Service function to update a butterfly's information by its ID
# It calls the update_butterfly function with the butterfly ID, updated data, and the database session
def update_butterfly_serv(butterfly_id: int, butterfly_update: ButterflyCreate, db: Session = Depends(get_db)):
    return update_butterfly(butterfly_id, butterfly_update, db)