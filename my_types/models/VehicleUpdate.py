from dataclasses import dataclass
from typing import Optional


@dataclass
class VehicleUpdate:
    """
    Represents an update for a vehicle.
    """
    id: str  # Vehicle ID
    customerId: Optional[str] = None  # Assigned customer ID
