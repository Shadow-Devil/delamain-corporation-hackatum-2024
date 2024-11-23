from model.backend.ScenarioDTO import ScenarioDTO
from model.scenario_runner.UpdateScenario import UpdateScenario
from model.scenario_runner.VehicleUpdate import VehicleUpdate
from scenario_runner_api import update_scenario
import math


def assign(scenario: ScenarioDTO) -> list[VehicleUpdate]:
    ret = []
    shortest_paths = dict()
    for v in scenario.vehicles:
        for c in scenario.customers:
            distance = v.remainingTravelTime * v.vehicleSpeed + math.dist((v.coordX, v.coordY), (c.coordX, c.coordY))
            best, d = shortest_paths.get(v)
            if not d or distance < best:
                shortest_paths[v] = (c, distance)

    for v in shortest_paths:
        c, d = shortest_paths[v]
        if v.isAvailable and c.awaitingService:
            ret.append(VehicleUpdate(id=v.id, customerId=c.id))
            c.awaitingService = False
        else:
            pass
    return ret


def step(scenario: ScenarioDTO):
    customers = list(filter(lambda c: c.awaitingService, scenario.customers))
    updates = []
    if not customers and any([v.isAvailable for v in scenario.vehicles]):
        updates = assign(scenario)
    update_scenario(scenario.id, UpdateScenario(vehicles=updates))
