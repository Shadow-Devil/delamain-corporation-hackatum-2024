from typing import Optional

from pydantic import BaseModel

from my_types.models.Customer import Customer
from my_types.models.Vehicle import Vehicle


class Scenario(BaseModel):
    """
    Represents a scenario containing vehicles and customers.
    """
    id: str  # Scenario ID (required)
    startTime: Optional[str] = None  # Start time of the scenario (optional)
    endTime: Optional[str] = None  # End time of the scenario (optional)
    status: Optional[str] = None  # Status of the scenario (optional)
    vehicles: Optional[list[Vehicle]] = None  # List of vehicles in the scenario (optional)
    customers: Optional[list[Customer]] = None  # List of customers in the scenario (optional)
