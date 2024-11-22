from dataclasses import dataclass
from VehicleDataDto import VehicleDataDto


@dataclass
class ScenarioMetadataDTO:
    """
    The scenario metadata data transfer object.
    """
    endTime: str
    id: str
    startTime: str
    status: str
    vehicleData: VehicleDataDto
