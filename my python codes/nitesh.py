from fastapi import APIRouter
from geopy.distance import geodesic

router = APIRouter()

@router.get("/smart_eta")
def get_smart_eta(start_lat: float, start_lon: float, end_lat: float, end_lon: float, speed: float):
    # Step 1: Distance
    distance = geodesic((start_lat, start_lon), (end_lat, end_lon)).km

    # Step 2: Base ETA
    if speed <= 0: 
        return {"error": "Invalid speed"}
    base_eta = (distance / speed) * 60

    # Step 3: Apply factors
    traffic_factor = 1.2
    weather_factor = 1.1
    stop_factor = 1.15

    smart_eta = base_eta * traffic_factor * weather_factor * stop_factor

    return {
        "distance_km": round(distance, 2),
        "base_eta_min": round(base_eta, 2),
        "smart_eta_min": round(smart_eta, 2)
    }
