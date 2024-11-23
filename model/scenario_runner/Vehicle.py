from dataclasses import dataclass
from typing import Optional


@dataclass
class Vehicle:
    """
    Represents a vehicle in the scenario.
    """
    id: str  # Vehicle ID
    coordX: float  # X Coordinate of the vehicle
    coordY: float  # Y Coordinate of the vehicle
    isAvailable: Optional[bool] = None  # Availability of the vehicle
    vehicleSpeed: Optional[float] = None  # Speed of the vehicle
    customerId: Optional[str] = None  # ID of the customer assigned to the vehicle
    remainingTravelTime: Optional[float] = None  # Remaining travel time for the vehicle
    distanceTravelled: Optional[float] = None  # Total distance the vehicle has travelled
    activeTime: Optional[float] = None  # Total active time of the vehicle
    numberOfTrips: Optional[int] = None  # Total number of trips made by the vehicle
