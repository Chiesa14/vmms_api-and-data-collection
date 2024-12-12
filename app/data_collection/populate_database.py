import random

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.schedule import MaintenanceSchedule
from app.models.vehicle import Vehicle

# Initialize Faker and Database Connection
fake = Faker()
DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost/vmms_api"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db = Session()


# Generate Vehicles
def generate_vehicles(num_vehicles):
    vehicles = []
    for _ in range(num_vehicles):
        vehicles.append(
            Vehicle(
                make=random.choice(['Toyota', 'Honda', 'Ford', 'BMW', 'Volvo', 'Mercedes']),
                vehicle_name=fake.name(),
                model=random.choice(['Automatic', 'Manual']),
                year=random.randint(2000, 2023),
                vin=fake.unique.bothify(text='??####????????'),
                color=random.choice(['Red', 'Blue', 'Green', 'Black', 'White', None]),
                type=random.choice(['Car', 'Motorcycle'])
            )
        )
    return vehicles


# Generate Maintenance Schedules
def generate_maintenance_schedules(vehicle_ids, num_schedules):
    schedules = []
    for _ in range(num_schedules):
        due_date = fake.date_between(start_date='-5y', end_date='+5y') if random.choice([True, False]) else None

        schedules.append(
            MaintenanceSchedule(
                vehicle_id=random.choice(vehicle_ids),
                task_name=random.choice(['Oil Change', 'Tire Rotation', 'Brake Inspection', 'Checking', 'Updating']),
                due_date=due_date,
                completed=random.choice([True, False, ])
            )
        )
    return schedules


# Insert Data in Batches
def insert_data_in_batches(session, data, batch_size=1000):
    for i in range(0, len(data), batch_size):
        session.bulk_save_objects(data[i:i + batch_size])
        session.commit()


# Main Function
def main():
    print("Generating vehicles...")
    vehicles = generate_vehicles(500000)
    insert_data_in_batches(db, vehicles)
    print(f"Inserted {len(vehicles)} vehicles.")

    print("Generating maintenance schedules...")
    vehicle_ids = [v.id for v in db.query(Vehicle).all()]
    schedules = generate_maintenance_schedules(vehicle_ids, 500000)
    insert_data_in_batches(db, schedules)
    print(f"Inserted {len(schedules)} maintenance schedules.")

    print("Data population completed!")


if __name__ == "__main__":
    main()
