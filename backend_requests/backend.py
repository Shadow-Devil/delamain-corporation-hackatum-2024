import requests

from model.scenario_runner.Scenario import Scenario

URL = 'http://localhost:8080'

def get_all_scenarios() -> list[Scenario]:
    return list(map(Scenario.model_validate, requests.get(URL + '/scenarios').json()))

def get_scenario(scenario_id: str) -> Scenario:
    return Scenario.model_validate(requests.get(URL + '/scenarios/' + scenario_id).json())

