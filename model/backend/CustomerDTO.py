from pydantic import BaseModel


class CustomerDTO(BaseModel):
    """
    The customer data transfer object.
    """
    awaitingService: bool
    coordX: float
    coordY: float
    destinationX: float
    destinationY: float
    id: str
