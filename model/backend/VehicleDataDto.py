from pydantic import BaseModel


class VehicleDataDto(BaseModel):
    """
    The vehicle data transfer object.
    """
    id: str
    totalTravelTime: int
    totalTrips: int
    travelTimes: str
