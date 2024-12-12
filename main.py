from fastapi import FastAPI

from app.database import Base, engine
from app.views.vehicle_routes import router as vehicle_router
from app.views.schedule_routes import router as schedule_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(vehicle_router, prefix="/api/v1", tags=["campaigns"])
app.include_router(schedule_router, prefix="/maintenance", tags=["Maintenance Schedules"])

