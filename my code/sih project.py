# sih_project.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import threading
import time
import random

# ---------------- Database Setup ----------------
DATABASE_URL = "sqlite:///./bus_tracking.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- Models ----------------
class Bus(Base):
    __tablename__ = "buses"
    id = Column(Integer, primary_key=True, index=True)
    bus_number = Column(String, unique=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)

Base.metadata.create_all(bind=engine)

# ---------------- App Setup ----------------
app = FastAPI(title="Real-Time Bus Tracking")

# ---------------- Real-time Simulation ----------------
def simulate_bus_movement():
    db = next(get_db())
    while True:
        buses = db.query(Bus).all()
        for bus in buses:
            bus.latitude += random.uniform(-0.001, 0.001)
            bus.longitude += random.uniform(-0.001, 0.001)
        db.commit()
        time.sleep(5)  # update every 5 seconds

threading.Thread(target=simulate_bus_movement, daemon=True).start()

# ---------------- API Endpoints ----------------
@app.post("/buses/")
def create_bus(bus_number: str, latitude: float, longitude: float, db: Session = Depends(get_db)):
    existing = db.query(Bus).filter(Bus.bus_number == bus_number).first()
    if existing:
        raise HTTPException(status_code=400, detail="Bus already exists")
    new_bus = Bus(bus_number=bus_number, latitude=latitude, longitude=longitude)
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)
    return {"id": new_bus.id, "bus_number": new_bus.bus_number, "latitude": new_bus.latitude, "longitude": new_bus.longitude}

@app.get("/buses/")
def get_buses(db: Session = Depends(get_db)):
    buses = db.query(Bus).all()
    return [{"id": b.id, "bus_number": b.bus_number, "latitude": b.latitude, "longitude": b.longitude} for b in buses]

@app.get("/buses/{bus_id}")
def get_bus(bus_id: int, db: Session = Depends(get_db)):
    bus = db.query(Bus).filter(Bus.id == bus_id).first()
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return {"id": bus.id, "bus_number": bus.bus_number, "latitude": bus.latitude, "longitude": bus.longitude}

@app.put("/buses/{bus_id}")
def update_bus(bus_id: int, latitude: float, longitude: float, db: Session = Depends(get_db)):
    bus = db.query(Bus).filter(Bus.id == bus_id).first()
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    bus.latitude = latitude
    bus.longitude = longitude
    db.commit()
    db.refresh(bus)
    return {"id": bus.id, "bus_number": bus.bus_number, "latitude": bus.latitude, "longitude": bus.longitude}
