from model.backend import CustomerDTO, StandardMagentaVehicleDTO
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment

def commision(vehicals:list[StandardMagentaVehicleDTO.StandardMagentaVehicleDTO],customers:list[CustomerDTO.CustomerDTO]):
    vehicals_coordinate = extract_coordinate(vehicals)
    customer_coordinate = extract_coordinate(customers)

    distance_matrix = cdist(customer_coordinate, vehicals_coordinate, metric='euclidean')


def extract_coordinate(data): # hier können wir eine "Locatable" Interface erstellen
    coordinates = list()
    for item in data:
        coordinates.append([item.coordX,item.coordY])
    return coordinates