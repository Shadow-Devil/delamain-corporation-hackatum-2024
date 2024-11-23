from pydantic import BaseModel

from model.backend.CustomerDTO import CustomerDTO
from model.backend.StandardMagentaVehicleDTO import StandardMagentaVehicleDTO


class ScenarioDTO(BaseModel):
    """
    The scenario data transfer object.
    """
    customers: list[CustomerDTO]
    endTime: str | None
    id: str | None
    startTime: str | None
    status: str | None
    vehicles: list[StandardMagentaVehicleDTO]
