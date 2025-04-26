from sqlalchemy.orm import Session
from models.Butterfly import Butterfly
from Schemes.Butterfly_Scheme import ButterflyCreate

@app.get("/butterfly/")
def read_butterflys(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    butterfly = db.query(Butterfly).offset(skip).limit(limit).all()
    return butterfly


@app.post("/butterfly/", status_code=201)
def create_butterfly(name: str, description: str = None, db: Session = Depends(get_db)):
    butterfly = Butterfly(name=name, description=description)
    db.add(butterfly)
    db.commit()
    db.refresh(butterfly)
    return butterfly


@app.get("/butterfly/{butterfly_id}")
def read_butterfly(butterfly_id: int, db: Session = Depends(get_db)):
    butterfly = db.query(Butterfly).filter(Butterfly.id == butterfly_id).first()
    if butterfly is None:
        raise HTTPException(status_code=404, detail="Butterfly not found")
    return butterfly


@app.delete("/butterfly/{butterfly_id}")
def delete_butterfly(butterfly_id: int, db: Session = Depends(get_db)):
    butterfly = db.query(Butterfly).filter(Butterfly.id == butterfly_id).first()
    if butterfly is None:
        raise HTTPException(status_code=404, detail="Butterfly not found")
    db.delete(butterfly)
    db.commit()
    return {"message": "Butterfly deleted successfully"}