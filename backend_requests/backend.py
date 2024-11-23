import requests
from typing import List

from model.backend.CustomerDTO import CustomerDTO
from model.backend.ScenarioDTO import ScenarioDTO
from model.backend.ScenarioMetadataDTO import ScenarioMetadataDTO
from model.backend.VehicleDataDto import VehicleDataDto

URL = 'http://localhost:8080'


# customers
def get_customer(customer_id: str) -> CustomerDTO:
    return CustomerDTO.model_validate(requests.get(f'{URL}/customers/{customer_id}').json())


def get_customers(scenario_id: str) -> list[CustomerDTO]:
    return list(map(CustomerDTO.model_validate, requests.get(f'{URL}/scenarios/{scenario_id}/customers').json()))


# scenarios
def get_scenario_metadata(scenario_id: str) -> ScenarioMetadataDTO:
    return ScenarioMetadataDTO.model_validate(requests.get(f'{URL}/scenario/{scenario_id}/metadata').json())


def create_scenario(vehicles: int, customers: int):
    return ScenarioDTO.model_validate(requests.post(f'{URL}/scenario/create', params={
        "numberOfVehicles": vehicles,
        "numberOfCustomers": customers
    }).json())


def get_scenarios() -> List[ScenarioDTO]:
    return list(map(ScenarioDTO.model_validate, requests.get(f'{URL}/scenarios').json()))


def delete_scenario(scenario_id: str) -> None:
    requests.delete(f'{URL}/scenarios/{scenario_id}')


def get_scenario(scenario_id: str) -> ScenarioDTO:
    return ScenarioDTO.model_validate(requests.get(f'{URL}/scenarios/{scenario_id}').json())


# vehicles
def get_vehicles(scenario_id: str) -> list[VehicleDataDto]:
    return list(map(VehicleDataDto.model_validate, requests.get(f'{URL}/scenarios/{scenario_id}/vehicles').json()))


def get_vehicle(vehicle_id: str) -> VehicleDataDto:
    return VehicleDataDto.model_validate(requests.get(f'{URL}/vehicles/{vehicle_id}').json())
