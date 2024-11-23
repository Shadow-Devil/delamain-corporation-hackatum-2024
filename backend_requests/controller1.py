from typing import List

from backend_requests.scenario_runner_api import update_scenario
from model.backend.ScenarioDTO import ScenarioDTO
from model.backend.StandardMagentaVehicleDTO import StandardMagentaVehicleDTO
from model.backend.CustomerDTO import CustomerDTO
from model.scenario_runner.UpdateScenario import UpdateScenario
from model.scenario_runner.VehicleUpdate import VehicleUpdate
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
import numpy as np

piority_id = None
piority_customer=[] # muss auf leer setzen wenn senario wechselt
vehicle_queue:list[str] = []
waiting_customer:list[CustomerDTO] = [] # assigned but waiting
assigned_customer:list[CustomerDTO] = []

def assign(scenario: ScenarioDTO,ratio:float) -> list[StandardMagentaVehicleDTO]:
    customers = scenario.customers
    print(len(customers))
    vehicles = scenario.vehicles
    if len(vehicles)>= len(customers): # if there is more taxi than customers, assign taxis based on minimal general waiting time
        customers_position = [[c.coordX,c.coordY] for c in customers]
        vehicles_position = [[v.coordX,v.coordY] for v in vehicles]
        distance = cdist(customers_position, vehicles_position, metric='euclidean')
        c_indices,v_indices = linear_sum_assignment(distance)
        for index_comb in zip(v_indices,c_indices):
            print(index_comb)
            vehicles[index_comb[0]].customerId = customers[index_comb[1]].id
    else: # else, this algorithm will always run this part to assign taxi to one customer
        if list(filter(lambda v: v.customerId is None,vehicles)) == []: # the piority will increase by ratio when customers are waiting
            for i,c in enumerate(customers):
                if c.awaitingService and c not in waiting_customer and c not in assigned_customer:
                    global piority_customer
                    piority_customer[i] += ratio
        else: # if there is at least one taxi free now, we evaluate the distance based on the waiting list for a taxi
            free_vehicles: list[StandardMagentaVehicleDTO] = list(filter(lambda v: v.customerId is None,vehicles))
            for v in free_vehicles:
                if v.id in vehicle_queue:
                    index = vehicle_queue.index(v.id)# if a vehicle is free, we check if there is already a customer waiting for this taxi
                    v.customerId = waiting_customer[index].id
                    vehicle_queue.pop(index)
                    waiting_customer.pop(index)
                    print("removed from waiting but assigned list:", len(waiting_customer))
            print("current vehicle queue:", len(vehicle_queue))
            print("waiting but assigned: ", len(waiting_customer))
            awaiting_customers = list()
            awaiting_customers_index = list()
            awaiting_customers_position = list()
            for i,c in enumerate(customers): # recording all the waiting customer
                if c.awaitingService and c not in waiting_customer and c not in assigned_customer:
                    awaiting_customers.append(c)
                    awaiting_customers_index.append(i)
                    awaiting_customers_position.append([c.coordX,c.coordY])
            if awaiting_customers: # if there are waiting customers
                #print(awaiting_customers_position)
                available_vehicles = list()
                available_vehicles_index = list()
                available_vehicles_position = list()
                for i,v in enumerate(vehicles): # we take all the vehicles as long as it is working and not assigned to a waiting customer
                    if v.id not in vehicle_queue:
                        available_vehicles.append(v)
                        available_vehicles_index.append(i)
                        available_vehicles_position.append([v.coordX,v.coordY])
                free_v_index = list()
                for i, v in enumerate(available_vehicles):  # recording all the index of free vehicles in the available vehicles
                    if v.customerId is None:
                        free_v_index.append(i)
                #calculate weighted distance based on piority
                end_positions,distance_to_go = base_distance_calculator(available_vehicles,customers)
                distance_total = cdist(awaiting_customers_position,end_positions, metric='euclidean') + distance_to_go
                #print(piority_customer, awaiting_customers_index)
                distance_total[:,free_v_index]/=np.array(piority_customer)[awaiting_customers_index].reshape(-1,1)
                if len(available_vehicles)>= len(awaiting_customers):
                    c_indices,v_indices = linear_sum_assignment(distance_total)
                else:
                    v_indices,c_indices = linear_sum_assignment(distance_total.T)
                #After calculated the weighted distance, assign taxis to the best customers using the waiting list of each taxi
                for i,v_index in enumerate(v_indices):
                    if vehicles[available_vehicles_index[v_index]].customerId is None: # if the chosen vehicle is really free
                        vehicles[available_vehicles_index[v_index]].customerId = customers[awaiting_customers_index[c_indices[i]]].id # assign a taxi to a customer
                        assigned_customer.append(customers[awaiting_customers_index[c_indices[i]]])
                    else:
                        #if vehicles[available_vehicles_index[v_index]].id in vehicle_queue:
                        #    ix = vehicle_queue.index(vehicles[available_vehicles_index[v_index]].id)
                        #    waiting_customer[ix].append(customers[awaiting_customers_index[c_indices[i]]])
                        #else:
                        vehicle_queue.append(vehicles[available_vehicles_index[v_index]].id)
                        waiting_customer.append(customers[awaiting_customers_index[c_indices[i]]])
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
        updates = assign(scenario,0.5)
    updates_ = list(filter(lambda x: x.customerId is not None, map(lambda x: VehicleUpdate.model_validate(x.model_dump()), updates)))
    #print(str(updates_))
    update_scenario(scenario.id, UpdateScenario(vehicles=updates_))
