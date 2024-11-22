from dataclasses import dataclass
from typing import Optional


@dataclass
class Customer:
    """
    Represents a customer in the scenario.
    """
    id: str  # Customer ID
    coordX: Optional[float] = None  # Customer X coordinate
    coordY: Optional[float] = None  # Customer Y coordinate
    destinationX: Optional[float] = None  # Customer destination X coordinate
    destinationY: Optional[float] = None  # Customer destination Y coordinate
    awaitingService: Optional[bool] = None  # Whether the customer is awaiting service
