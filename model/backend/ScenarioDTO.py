from typing import Optional

from pydantic import BaseModel

from model.backend.CustomerDTO import CustomerDTO
from model.backend.StandardMagentaVehicleDTO import StandardMagentaVehicleDTO


class ScenarioDTO(BaseModel):
    """
    The scenario data transfer object.
    """
    customers: list[CustomerDTO]
    endTime: Optional[str]
    id: Optional[str]
    startTime: Optional[str]
    status: Optional[str]
    vehicles: list[StandardMagentaVehicleDTO]
