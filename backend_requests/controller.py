from model.backend.ScenarioDTO import ScenarioDTO
from model.scenario_runner.UpdateScenario import UpdateScenario
from model.scenario_runner.VehicleUpdate import VehicleUpdate
from scenario_runner_api import update_scenario


def assign(scenario: ScenarioDTO) -> list[VehicleUpdate]:
    return []


def step(scenario: ScenarioDTO):
    customers = list(filter(lambda c: c.awaitingService, scenario.customers))
    updates = []
    if not customers and any([v.isAvailable for v in scenario.vehicles]):
        updates = assign(scenario)
    update_scenario(scenario.id, UpdateScenario(vehicles=updates))
