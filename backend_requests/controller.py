from app import app
from backend_requests.scenario_runner_api import update_scenario
from model.backend.ScenarioDTO import ScenarioDTO
from model.scenario_runner.UpdateScenario import UpdateScenario
from model.scenario_runner.VehicleUpdate import VehicleUpdate
import math


def assign(scenario: ScenarioDTO) -> list[VehicleUpdate]:
    ret = []
    shortest_paths = dict()
    for v in scenario.vehicles:
        for c in scenario.customers:
            distance = (v.remainingTravelTime or 0) * (v.vehicleSpeed or 0) + math.dist((v.coordX, v.coordY), (c.coordX, c.coordY))
            best, d = shortest_paths.get(v.id)
            if not d or distance < best:
                shortest_paths[v.id] = (c, distance)

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
    print("updating vehicles: " + str(updates))
    update_scenario(scenario.id, UpdateScenario(vehicles=updates))
