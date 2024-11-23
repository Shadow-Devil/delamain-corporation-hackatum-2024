from typing import Optional
from pydantic import BaseModel

from model.scenario_runner.VehicleUpdate import VehicleUpdate


class UpdateScenario(BaseModel):
    """
    Represents an update to a scenario, focusing on vehicles.
    """
    vehicles: Optional[VehicleUpdate] = None  # List of updated vehicles
