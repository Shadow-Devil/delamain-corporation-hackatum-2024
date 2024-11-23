import requests
from typing import List

from model.scenario_runner.Scenario import Scenario
from model.scenario_runner.Customer import Customer
from model.backend.ScenarioMetadataDTO import ScenarioMetadataDTO
from model.scenario_runner.Vehicle import Vehicle

URL = 'http://localhost:8080'


# customers
def get_customer(customer_id: str) -> Customer:
    return Customer.model_validate(requests.get(f'{URL}/customers/{customer_id}').json())


def get_customers(scenario_id: str) -> List[Customer]:
    return list(map(Customer.model_validate, requests.get(f'{URL}/scenarios/{scenario_id}/customers').json()))


# scenarios
def get_scenario_metadata(scenario_id: str) -> ScenarioMetadataDTO:
    return ScenarioMetadataDTO.model_validate(requests.get(f'{URL}/scenario/{scenario_id}/metadata').json())


def create_scenario() -> Scenario:
    return Scenario.model_validate(requests.post(f'{URL}/scenario/create').json())


def get_scenarios() -> List[Scenario]:
    return list(map(Scenario.model_validate, requests.get(f'{URL}/scenarios').json()))


def delete_scenario(scenario_id: str) -> None:
    requests.delete(f'{URL}/scenarios/{scenario_id}')


def get_scenario(scenario_id: str) -> Scenario:
    return Scenario.model_validate(requests.get(f'{URL}/scenarios/{scenario_id}').json())


# vehicles
def get_vehicles(scenario_id: str) -> List[Vehicle]:
    return list(map(Vehicle.model_validate, requests.get(f'{URL}/scenarios/{scenario_id}/vehicles').json()))


def get_vehicle(vehicle_id: str) -> Vehicle:
    return Vehicle.model_validate(requests.get(f'{URL}/vehicles/{vehicle_id}').json())
