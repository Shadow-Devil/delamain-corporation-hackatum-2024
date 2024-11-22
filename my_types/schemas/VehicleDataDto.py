from dataclasses import dataclass


@dataclass
class VehicleDataDto:
    """
    The vehicle data transfer object.
    """
    id: str
    totalTravelTime: int
    totalTrips: int
    travelTimes: str
