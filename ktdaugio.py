from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class CreateFlight(BaseModel):
    flight_number: str = Field(...)
    destination: str = Field(...)
    available_seats: int = Field(...)
    status: str = Field(default="scheduled")

flights_db = [
    {"id": 1, "flight_number": "VN-213", "destination": "Da Nang", "available_seats": 45, "status": "scheduled"},
    {"id": 2, "flight_number": "VJ-122", "destination": "Phu Quoc", "available_seats": 12, "status": "scheduled"},
    {"id": 3, "flight_number": "VN-322", "destination": "Ha Noi", "available_seats": 18, "status": "landed"},
    {"id": 4, "flight_number": "VJ-220", "destination": "Thanh pho Ho Chi Minh", "available_seats": 20, "status": "delayed"}
]


@app.get("/flights")
async def get_flights(status: Optional[str] = None):
    if status is None:
        filtered_flights = flights_db
    else:
        filtered_flights = [flight for flight in flights_db if flight["status"] == status]
    return {
        "statusCode": 200,
        "message": "Lấy danh sách chuyến bay thành công",
        "data": filtered_flights,
        "error": None,
        "path": "/flights",
    }


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return {
            "statusCode": 404,
            "message": "Lỗi: Không tìm thấy mã chuyến bay yêu cầu để hủy!",
            "data": None,
            "error": "ERR-AIR-02: Target flight ID is missing from system scope.",
            "path": request.url.path,
        }
    return {"detail": exc.detail}

@app.post('/flights', status_code=201)
async def add_flights(flc: CreateFlight):
    new_flight = {
        "id":
    }
    
    
    
    
    

@app.delete('/flights/{flight_id}')
async def delete_flights(flight_id: int):
    for i, item in enumerate(flights_db):
        if item["id"] == flight_id:
            flights_db.pop(i)
            return {
                "statusCode": 200,
                "message": "Hủy chuyến bay thành công!",
                "data": None,
                "error": None,
                "path": f"/flights/{flight_id}",
            }
    raise HTTPException(status_code=404)
    
