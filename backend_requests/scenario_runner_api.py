import requests
from typing import Any

from model.scenario_runner.Scenario import Scenario
from model.scenario_runner.UpdateScenario import UpdateScenario

URL = 'http://localhost:8090'


# Scenarios
def get_scenario(scenario_id: str) -> Scenario | None:
    response = requests.get(f'{URL}/Scenarios/get_scenario/{scenario_id}')
    if response.status_code == 404:
        return None
    return Scenario.model_validate(response.json())


def initialize_scenario(payload: Scenario, db_scenario_id: str = None):
    response = requests.post(
        f'{URL}/Scenarios/initialize_scenario', json=payload.model_dump(), params={'db_scenario_id': db_scenario_id})
    if response.status_code != 200:
        raise Exception(response.text)


def update_scenario(scenario_id: str, payload: UpdateScenario) -> Scenario:
    return Scenario.model_validate(requests.put(f'{URL}/Scenarios/update_scenario/{scenario_id}', json=payload.json).json())


# Runner
def launch_scenario(scenario_id: str, speed: float = 0.2) -> Any:
    return requests.post(f'{URL}/Runner/launch_scenario/{scenario_id}', params={'speed': speed}).json()
