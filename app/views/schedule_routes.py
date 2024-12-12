from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schedule import (
    MaintenanceScheduleCreate,
    MaintenanceScheduleUpdate,
    MaintenanceScheduleResponse
)
from app.controllers.schedule import (
    create_schedule,
    update_schedule,
    delete_schedule,
    list_schedules,
    get_schedule, get_schedules_by_vehicle_id
)

router = APIRouter()


@router.post("/", response_model=MaintenanceScheduleResponse)
def create_maintenance_schedule(
    schedule_data: MaintenanceScheduleCreate, db: Session = Depends(get_db)
):
    return create_schedule(db, schedule_data)


@router.put("/{schedule_id}", response_model=MaintenanceScheduleResponse)
def update_maintenance_schedule(
    schedule_id: int, schedule_data: MaintenanceScheduleUpdate, db: Session = Depends(get_db)
):
    schedule = update_schedule(db, schedule_id, schedule_data)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule


@router.delete("/{schedule_id}", response_model=dict)
def delete_maintenance_schedule(schedule_id: int, db: Session = Depends(get_db)):
    schedule = delete_schedule(db, schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return {"message": "Schedule deleted successfully"}


@router.get("/", response_model=list[MaintenanceScheduleResponse])
def list_maintenance_schedules(
    vehicle_id: int = Query(None), completed: bool = Query(None), db: Session = Depends(get_db)
):
    return list_schedules(db, vehicle_id, completed)


@router.get("/{schedule_id}", response_model=MaintenanceScheduleResponse)
def get_maintenance_schedule(schedule_id: int, db: Session = Depends(get_db)):
    schedule = get_schedule(db, schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule


@router.get("/vehicle/{vehicle_id}", response_model=list[MaintenanceScheduleResponse])
def get_schedules_for_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    schedules = get_schedules_by_vehicle_id(db, vehicle_id)
    if not schedules:
        raise HTTPException(status_code=404, detail="No schedules found for the given vehicle_id")
    return schedules
