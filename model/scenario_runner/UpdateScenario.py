from dataclasses import dataclass
from typing import Optional
from VehicleUpdate import VehicleUpdate


@dataclass
class UpdateScenario:
    """
    Represents an update to a scenario, focusing on vehicles.
    """
    vehicles: Optional[VehicleUpdate] = None  # List of updated vehicles
