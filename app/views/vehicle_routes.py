from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.vehicle import VehicleCreate, VehicleResponse
from app.controllers.vehicle import create_vehicle, get_vehicle, get_vehicles
from app.database import get_db  # assuming your database session is in database.py

router = APIRouter()

@router.post("/vehicles/", response_model=VehicleResponse)
def create_vehicle_route(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db=db, vehicle=vehicle)

@router.get("/vehicles/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle_route(vehicle_id: int, db: Session = Depends(get_db)):
    return get_vehicle(db=db, vehicle_id=vehicle_id)

@router.get("/vehicles/", response_model=list[VehicleResponse])
def get_vehicles_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_vehicles(db=db, skip=skip, limit=limit)
