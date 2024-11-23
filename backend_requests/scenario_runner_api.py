import requests
from typing import Any

from model.scenario_runner.Scenario import Scenario
from model.scenario_runner.UpdateScenario import UpdateScenario

URL = 'http://localhost:8080'


# Scenarios
def get_scenario(scenario_id: str) -> Scenario:
    return Scenario.model_validate(requests.get(f'{URL}/Scenarios/get_scenario/{scenario_id}').json())


def initialize_scenario(payload: Scenario, db_scenario_id: str = None) -> Scenario:
    return Scenario.model_validate(requests.post(
        f'{URL}/Scenarios/initialize_scenario', json=payload.json, params={'db_scenario_id': db_scenario_id}).json())


def update_scenario(scenario_id: str, payload: UpdateScenario) -> Scenario:
    return Scenario.model_validate(requests.put(f'{URL}/Scenarios/update_scenario/{scenario_id}', json=payload.json).json())


# Runner
def launch_scenario(scenario_id: str, speed: float = 0.2) -> Any:
    return requests.post(f'{URL}/Runner/launch_scenario/{scenario_id}', params={'speed': speed}).json()
