from typing import Optional
from VehicleUpdate import VehicleUpdate
from pydantic import BaseModel


class UpdateScenario(BaseModel):
    """
    Represents an update to a scenario, focusing on vehicles.
    """
    vehicles: Optional[VehicleUpdate] = None  # List of updated vehicles
