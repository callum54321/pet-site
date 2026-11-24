from pydantic import BaseModel, ConfigDict


# Input validation creating new pet item
class PetCreate(BaseModel):
    name: str
    age: int
    species: str
    description: str
    url: str
    location: str


# Output validation pet response
class PetResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )  # Allow pydantic to read data directly from ORM
    id: int
    name: str
    age: int
    species: str
    description: str
    url: str
    location: str
