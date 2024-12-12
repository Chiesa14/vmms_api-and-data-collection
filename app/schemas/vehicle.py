from pydantic import BaseModel
from typing import Optional

class VehicleBase(BaseModel):
    make: str
    vehicle_name: str
    model: str
    year: int
    vin: str
    color: Optional[str] = None
    type: str

    class Config:
        orm_mode = True  # Tells Pydantic to work with SQLAlchemy models

class VehicleCreate(VehicleBase):
    pass

class VehicleResponse(VehicleBase):
    id: int
    vehicle_name: str

    class Config:
        orm_mode = True
