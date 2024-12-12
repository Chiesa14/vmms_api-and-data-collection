from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.schedule import MaintenanceSchedule
from app.schemas.schedule import MaintenanceScheduleCreate, MaintenanceScheduleUpdate


def create_schedule(db: Session, schedule_data: MaintenanceScheduleCreate):
    try:
        # Create a new schedule
        schedule = MaintenanceSchedule(**schedule_data.dict())
        db.add(schedule)
        db.commit()
        db.refresh(schedule)
        return schedule
    except IntegrityError as e:
        db.rollback()
        # Handle foreign key or unique constraint errors
        if "FOREIGN KEY" in str(e.orig):
            raise HTTPException(
                status_code=400, detail="The specified vehicle does not exist."
            )
        else:
            raise HTTPException(
                status_code=500, detail="An unexpected database error occurred."
            )


def update_schedule(db: Session, schedule_id: int, schedule_data: MaintenanceScheduleUpdate):
    schedule = db.query(MaintenanceSchedule).filter(MaintenanceSchedule.id == schedule_id).first()
    if not schedule:
        return None

    for key, value in schedule_data.dict(exclude_unset=True).items():
        setattr(schedule, key, value)

    db.commit()
    db.refresh(schedule)
    return schedule


def delete_schedule(db: Session, schedule_id: int):
    schedule = db.query(MaintenanceSchedule).filter(MaintenanceSchedule.id == schedule_id).first()
    if schedule:
        db.delete(schedule)
        db.commit()
    return schedule


def list_schedules(db: Session, vehicle_id: Optional[int] = None, completed: Optional[bool] = None):
    query = db.query(MaintenanceSchedule)
    if vehicle_id:
        query = query.filter(MaintenanceSchedule.vehicle_id == vehicle_id)
    if completed is not None:
        query = query.filter(MaintenanceSchedule.completed == completed)

    schedules = query.all()

    return schedules


def get_schedule(db: Session, schedule_id: int):
    schedule = db.query(MaintenanceSchedule).filter(MaintenanceSchedule.id == schedule_id).first()

    return schedule


def get_schedules_by_vehicle_id(db: Session, vehicle_id: int):
    query = db.query(MaintenanceSchedule).filter(MaintenanceSchedule.vehicle_id == vehicle_id)
    schedules = query.all()

    return schedules
