from typing import Optional
from pydantic import BaseModel


class VehicleUpdate(BaseModel):
    """
    Represents an update for a vehicle.
    """
    id: str  # Vehicle ID
    customerId: Optional[str] = None  # Assigned customer ID
