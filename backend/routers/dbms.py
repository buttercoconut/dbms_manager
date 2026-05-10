# routers/dbms.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas, database

router = APIRouter(prefix="/dbms", tags=["dbms"])

# Create DBMS
@router.post("/", response_model=schemas.DBMSInDB, status_code=status.HTTP_201_CREATED)
def create_dbms(dbms: schemas.DBMSCreate, db: Session = Depends(database.get_db)):
    return crud.create_dbms(db, dbms)

# Read list
@router.get("/", response_model=List[schemas.DBMSInDB])
def read_dbms_list(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_dbms_list(db, skip=skip, limit=limit)

# Read single
@router.get("/{dbms_id}", response_model=schemas.DBMSInDB)
def read_dbms(dbms_id: int, db: Session = Depends(database.get_db)):
    dbms = crud.get_dbms(db, dbms_id)
    if dbms is None:
        raise HTTPException(status_code=404, detail="DBMS not found")
    return dbms

# Update
@router.put("/{dbms_id}", response_model=schemas.DBMSInDB)
def update_dbms(dbms_id: int, dbms_update: schemas.DBMSUpdate, db: Session = Depends(database.get_db)):
    dbms = crud.update_dbms(db, dbms_id, dbms_update)
    if dbms is None:
        raise HTTPException(status_code=404, detail="DBMS not found")
    return dbms

# Delete
@router.delete("/{dbms_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dbms(dbms_id: int, db: Session = Depends(database.get_db)):
    dbms = crud.delete_dbms(db, dbms_id)
    if dbms is None:
        raise HTTPException(status_code=404, detail="DBMS not found")
    return None
