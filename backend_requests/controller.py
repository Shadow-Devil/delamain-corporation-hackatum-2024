from model.backend.StandardMagentaVehicleDTO import StandardMagentaVehicleDTO
from model.backend.CustomerDTO import CustomerDTO
from model.backend.ScenarioDTO import ScenarioDTO
from scenario_runner_api import update_scenario


def assign(vehicles: list[StandardMagentaVehicleDTO], customers: list[CustomerDTO]) -> list[StandardMagentaVehicleDTO]:
    return []


def move(v: StandardMagentaVehicleDTO):
    pass


def step(scenario: ScenarioDTO):
    customers = list(filter(lambda c: c.awaitingService, scenario.customers))
    if not customers and any([v.isAvailable for v in scenario.vehicles]):
        scenario.vehicles = assign(scenario.vehicles, customers)
    move(scenario)
    update_scenario(scenario.id, scenario)
