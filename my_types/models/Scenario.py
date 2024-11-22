from dataclasses import dataclass
from typing import Optional
from Vehicle import Vehicle
from Customer import Customer


@dataclass
class Scenario:
    """
    Represents a scenario containing vehicles and customers.
    """
    id: str  # Scenario ID (required)
    startTime: Optional[str] = None  # Start time of the scenario (optional)
    endTime: Optional[str] = None  # End time of the scenario (optional)
    status: Optional[str] = None  # Status of the scenario (optional)
    vehicles: Optional[Vehicle] = None  # List of vehicles in the scenario (optional)
    customers: Optional[Customer] = None  # List of customers in the scenario (optional)
