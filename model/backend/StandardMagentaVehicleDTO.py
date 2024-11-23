from dataclasses import dataclass
from typing import Optional


@dataclass
class StandardMagentaVehicleDTO:
    """
    The vehicle data transfer object.
    """
    activeTime: Optional[int]
    coordX: Optional[float]
    coordY: Optional[float]
    customerId: Optional[str]
    distanceTravelled: Optional[float]
    id: Optional[str]
    isAvailable: Optional[bool]
    numberOfTrips: Optional[int]
    remainingTravelTime: Optional[int]
    vehicleSpeed: Optional[float]
