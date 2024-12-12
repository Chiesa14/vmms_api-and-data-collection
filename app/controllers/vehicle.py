from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle  # assuming the model is in models.py
from app.schemas.vehicle import VehicleCreate


def create_vehicle(db: Session, vehicle: VehicleCreate):
    try:
        db_vehicle = Vehicle(**vehicle.dict())
        db.add(db_vehicle)
        db.commit()
        db.refresh(db_vehicle)
        return db_vehicle
    except IntegrityError as e:
        db.rollback()
        if "Duplicate entry" in str(e.orig):
            raise HTTPException(
                status_code=400, detail="Vehicle with the same VIN already exists."
            )
        raise HTTPException(
            status_code=500, detail="An error occurred while creating the vehicle."
        )


def get_vehicle(db: Session, vehicle_id: int):
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found.")
    return vehicle


def get_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vehicle).offset(skip).limit(limit).all()
