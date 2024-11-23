from pydantic import BaseModel
from VehicleDataDto import VehicleDataDto


class ScenarioMetadataDTO(BaseModel):
    """
    The scenario metadata data transfer object.
    """
    endTime: str
    id: str
    startTime: str
    status: str
    vehicleData: VehicleDataDto
