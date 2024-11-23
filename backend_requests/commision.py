from model.backend import CustomerDTO, StandardMagentaVehicleDTO
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment

def commission(vehicles: list[StandardMagentaVehicleDTO.StandardMagentaVehicleDTO],
               customers: list[CustomerDTO.CustomerDTO],
               is_inital_commision: bool):
    # vehicle_coordinates = [(vehicle.coordX, vehicle.coordY) for vehicle in vehicles]
    # customer_coordinates = [(customer.coordX, customer.coordY) for customer in customers]
    # if len(vehicle_coordinates) == len(customer_coordinates):
    #     distance_matrix = cdist(customer_coordinates, vehicle_coordinates, metric='euclidean')
    #     customer_index,vehical_index = linear_sum_assignment(distance_matrix)
    #     assignment = zip(vehical_index,customer_index)
    #     for tupel in assignment:
    #         vehicles[tupel[0]].



def extract_coordinate(data): # hier können wir eine "Locatable" Interface erstellen
    coordinates = list()
    for item in data:
        coordinates.append([item.coordX,item.coordY])
    return coordinates