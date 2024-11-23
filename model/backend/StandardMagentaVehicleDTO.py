from dataclasses import dataclass


@dataclass
class StandardMagentaVehicleDTO:
    """
    The vehicle data transfer object.
    """
    activeTime: int | None
    coordX: float | None
    coordY: float | None
    customerId: str | None
    distanceTravelled: float | None
    id: str | None
    isAvailable: bool | None
    numberOfTrips: int | None
    remainingTravelTime: int | None
    vehicleSpeed: float | None
