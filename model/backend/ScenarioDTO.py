from dataclasses import dataclass
from CustomerDTO import CustomerDTO
from StandardMagentaVehicleDTO import StandardMagentaVehicleDTO


@dataclass
class ScenarioDTO:
    """
    The scenario data transfer object.
    """
    customers: [CustomerDTO]
    endTime: str
    id: str
    startTime: str
    status: str
    vehicles: [StandardMagentaVehicleDTO]
