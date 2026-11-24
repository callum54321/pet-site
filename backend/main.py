from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from schemas import PetCreate, PetResponse
from db.db import get_db, Pet
from sqlalchemy.orm import Session

app = FastAPI()


# Root endpoint
@app.get("/")
async def root():
    return {"message": "welcome to my api"}


# Get all pets endpoint (pets list)
@app.get("/pets", response_model=list[PetResponse])
async def get_all_pets(db: Session = Depends(get_db)):
    return db.query(Pet).all()


# Create new pet item endpoint
@app.post("/create-pet", response_model=PetResponse)
async def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    pet_item = Pet(**pet.model_dump())
    db.add(pet_item)
    db.commit()
    db.refresh(pet_item)

    return pet_item


# Get pet by id endpoint
@app.get("/pets/{id}", response_model=PetResponse)
async def get_pet(id: int, db: Session = Depends(get_db)):
    pet_item = db.query(Pet).filter(Pet.id == id).first()

    if pet_item is None:
        raise HTTPException(status_code=404, detail=f"Pet with id {id} not found.")

    return pet_item


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000, reload=True)
