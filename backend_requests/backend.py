from typing import Any

import requests

from my_types.models.Scenario import Scenario

URL = 'http://localhost:8080'

def get_all_scenarios() -> list[Scenario]:
    return list(map(Scenario.model_validate, requests.get(URL + '/scenarios').json()))

