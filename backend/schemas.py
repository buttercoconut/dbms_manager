# schemas.py
from pydantic import BaseModel, Field
from typing import Optional

class DBMSBase(BaseModel):
    name: str = Field(..., max_length=255)
    host: str
    port: int
    username: str
    password: str
    database: str
    is_active: Optional[bool] = True

class DBMSCreate(DBMSBase):
    pass

class DBMSUpdate(BaseModel):
    name: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    database: Optional[str] = None
    is_active: Optional[bool] = None

class DBMSInDB(DBMSBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True
