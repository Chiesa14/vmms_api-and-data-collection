from pydantic import BaseModel
from datetime import date
from typing import Optional


class MaintenanceScheduleBase(BaseModel):
    task_name: str
    due_date: Optional[date]
    completed: bool = False


class MaintenanceScheduleCreate(MaintenanceScheduleBase):
    vehicle_id: int


class MaintenanceScheduleUpdate(BaseModel):
    task_name: Optional[str]
    due_date: Optional[date]
    completed: Optional[bool]


class MaintenanceScheduleResponse(MaintenanceScheduleBase):
    id: int
    vehicle_id: int

    class Config:
        orm_mode = True
