from dataclasses import dataclass


@dataclass
class StandardMagentaVehicleDTO:
    """
    The vehicle data transfer object.
    """
    activeTime: int
    coordX: float
    coordY: float
    customerId: str
    distanceTravelled: float
    id: str
    isAvailable: bool
    numberOfTrips: int
    remainingTravelTime: int
    vehicleSpeed: float
