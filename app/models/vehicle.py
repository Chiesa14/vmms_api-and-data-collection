from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy.orm import relationship

from app.database import Base

class Vehicle(Base):
    __tablename__ = 'vehicles'

    # Choices for fields
    MAKE_CHOICES = [('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Ford', 'Ford'),
                    ('BMW', 'BMW'), ('Volvo', 'Volvo'), ('Mercedes', 'Mercedes')]
    MODEL_CHOICES = [('Automatic', 'Automatic'), ('Manual', 'Manual')]
    TYPE_CHOICES = [('Car', 'Car'), ('Motorcycle', 'Motorcycle')]

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String(20))
    vehicle_name = Column(String(50))
    model = Column(String(20))
    year = Column(SmallInteger)
    vin = Column(String(17), unique=True)
    color = Column(String(20), nullable=True)
    type = Column(String(20))

    maintenance_schedule = relationship("MaintenanceSchedule", back_populates="vehicle")



    def __repr__(self):
        return f"<Vehicle(vehicle_name={self.vehicle_name}, model={self.model}, vin={self.vin})>"
