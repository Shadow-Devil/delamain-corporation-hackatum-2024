from dataclasses import dataclass


@dataclass
class CustomerDTO:
    """
    The customer data transfer object.
    """
    awaitingService: bool
    coordX: float
    coordY: float
    destinationX: float
    destinationY: float
    id: str
