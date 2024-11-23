from typing import List

from backend_requests.scenario_runner_api import update_scenario
from model.backend.ScenarioDTO import ScenarioDTO
from model.backend.StandardMagentaVehicleDTO import StandardMagentaVehicleDTO
from model.scenario_runner.UpdateScenario import UpdateScenario
from model.scenario_runner.VehicleUpdate import VehicleUpdate
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
import numpy as np

piority_customer=[] # muss auf leer setzen wenn senario wechselt
vehicle_queue = []
waiting_customer = [] # assigned but waiting

def assign(scenario: ScenarioDTO,ratio:float) -> list[StandardMagentaVehicleDTO]:
    customers = scenario.customers
    print(len(customers))
    vehicles = scenario.vehicles
    if len(vehicles)>= len(customers):
        customers_position = [[c.coordX,c.coordY] for c in customers]
        vehicles_position = [[v.coordX,v.coordY] for v in vehicles]
        distance = cdist(customers_position, vehicles_position, metric='euclidean')
        v_indices,c_indices = linear_sum_assignment(distance)
        for index_comb in zip(v_indices,c_indices):
            print(index_comb)
            vehicles[index_comb[0]].customerId = customers[index_comb[1]].id
    else:
        if filter(lambda v: v.isAvailable,vehicles) == []:
            for i,c in enumerate(customers):
                if c.awaitingService and c not in waiting_customer:
                    global piority_customer
                    piority_customer[i] += 0.1
        else:
            free_vehicles = filter(lambda v: v.isAvailable,vehicles)
            for v in free_vehicles:
                if v.id in vehicle_queue:
                    index = vehicle_queue.index(v.id)
                    v.customerId = waiting_customer[index][0]
                    vehicle_queue.remove(v.id)
                    waiting_customer[index].pop(index)# 若顾客等待的列表为空，弹出这个列表
                    if waiting_customer[index] == []:
                        waiting_customer.pop(index)
            if free_vehicles == []:
                return vehicles
            else: # we assume there is now only one free vehicle
                free_v_index = 0
                for i,v in enumerate(vehicles):
                    if v.isAvailable:
                        free_v_index = i
                awaiting_customers = list()
                awaiting_customers_index = list()
                awaiting_customers_position = list()
                for i,c in enumerate(customers):
                    if c.awaitingService:
                        awaiting_customers.append(c)
                        awaiting_customers_index.append(i)
                        awaiting_customers_position.append([c.coordX,c.coordY])
                #计算加权距离列表
                end_positions,distance_to_go = base_distance_calculator(vehicles,customers)
                distance_total = cdist(awaiting_customers_position,end_positions, metric='euclidean') + distance_to_go
                distance_total[:,free_v_index]/=np.array(piority_customer)[awaiting_customers_index]
                if len(vehicles)>= len(awaiting_customers):
                    v_indices,c_indices = linear_sum_assignment(distance_total.T)
                else:
                    c_indices,v_indices = linear_sum_assignment(distance_total)
                #当我们完成了加权距离算法之后，进行车辆列表的填充或者分配
                for i,v_index in enumerate(v_indices):
                    if vehicles[v_index].isAvailable:
                        vehicles[v_index].customerId = customers[awaiting_customers_index[c_indices[i]]].id
                    else:
                        if vehicles[v_index].id in vehicle_queue:
                            ix = vehicle_queue.index(vehicles[v_index].id)
                            waiting_customer[ix].append(customers[awaiting_customers_index[c_indices[i]]])
                        else:
                            vehicle_queue.append(vehicles[v_index])
                            waiting_customer.append([customers[awaiting_customers_index[c_indices[i]]]])
    return vehicles


def base_distance_calculator(vehicles,customers):
    end_positions = list()
    distance_to_go = list()
    for v in vehicles:
        if v.customerId == None:
            end_positions.append([v.coordX,v.coordY])
            distance_to_go.append(0)
        else:
            customer_assigned = list(filter(lambda c: c.id == v.customerId,customers))
            end_positions.append([customer_assigned[0].destinationX,customer_assigned[0].destinationX])
            distance_to_go.append(np.linalg.norm(np.array([v.coordX,v.coordY]-np.array([customer_assigned[0].destinationX,customer_assigned[0].destinationX]))))
    return end_positions, distance_to_go

def step(scenario: ScenarioDTO):
    customers = list(filter(lambda c: c.awaitingService, scenario.customers))
    updates: List[StandardMagentaVehicleDTO] = []
    if customers and any([v.isAvailable for v in scenario.vehicles]):
        updates = assign(scenario,0.1)
    updates_ = map(lambda x: VehicleUpdate.model_validate(x.model_dump()), updates)
    print(str(updates_))
    update_scenario(scenario.id, UpdateScenario(vehicles=updates_))
