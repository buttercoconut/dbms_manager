# main.py
from fastapi import FastAPI
from . import database, models, routers

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="DBMS Manager API", version="0.1.0")

# Include routers
app.include_router(routers.dbms.router)

# Health check
@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}
