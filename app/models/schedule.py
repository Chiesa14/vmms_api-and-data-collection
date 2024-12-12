from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class MaintenanceSchedule(Base):
    __tablename__ = 'maintenance_schedule'

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    task_name = Column(String(255), nullable=False)
    due_date = Column(Date, nullable=True)
    completed = Column(Boolean,default=False)

    vehicle = relationship("Vehicle", back_populates="maintenance_schedule")

    def __repr__(self):
        return f"Scheduled: {self.task_name} for Vehicle ID {self.vehicle_id}"
