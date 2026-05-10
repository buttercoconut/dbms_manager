# crud.py
from sqlalchemy.orm import Session
from . import models, schemas

# Create a new DBMS record
def create_dbms(db: Session, dbms: schemas.DBMSCreate):
    db_obj = models.DBMS(**dbms.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Get DBMS by id
def get_dbms(db: Session, dbms_id: int):
    return db.query(models.DBMS).filter(models.DBMS.id == dbms_id).first()

# Get all DBMS records with pagination
def get_dbms_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DBMS).offset(skip).limit(limit).all()

# Update DBMS
def update_dbms(db: Session, dbms_id: int, dbms_update: schemas.DBMSUpdate):
    db_obj = db.query(models.DBMS).filter(models.DBMS.id == dbms_id).first()
    if not db_obj:
        return None
    for var, value in dbms_update.dict(exclude_unset=True).items():
        setattr(db_obj, var, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Delete DBMS
def delete_dbms(db: Session, dbms_id: int):
    db_obj = db.query(models.DBMS).filter(models.DBMS.id == dbms_id).first()
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj
