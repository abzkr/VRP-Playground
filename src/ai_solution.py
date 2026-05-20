from datasets import *
from itertools import combinations


# Function to calculate distance saved
def calculate_savings(distance_matrix):
    depot = 0
    savings = []

    for i, j in combinations(range(1, len(distance_matrix)), 2):
        saving = (
            distance_matrix[depot][i]
            + distance_matrix[depot][j]
            - distance_matrix[i][j]
        )
        savings.append((saving, i, j))

    return sorted(savings, reverse=True)

# Main function for each journey
def cvrp(distance_matrix, demands, vehicle_capacity, num_vehicles):
    n = len(distance_matrix)

    # Initial routes: one per customer
    routes = {i: [0, i, 0] for i in range(1, n)}
    route_loads = {i: demands[i] for i in range(1, n)}

    savings_list = calculate_savings(distance_matrix)

    for saving, i, j in savings_list:
        route_i = None
        route_j = None

        # Find routes containing i and j
        for key, route in routes.items():
            if route[1] == i and route[-2] == i:
                route_i = key
            if route[1] == j and route[-2] == j:
                route_j = key

        if route_i is None or route_j is None or route_i == route_j:
            continue

        # Check capacity constraint
        if route_loads[route_i] + route_loads[route_j] > vehicle_capacity:
            continue

        # Merge routes
        new_route = routes[route_i][:-1] + routes[route_j][1:]
        routes[route_i] = new_route
        route_loads[route_i] += route_loads[route_j]

        del routes[route_j]
        del route_loads[route_j]

    # Limit number of vehicles
    final_routes = list(routes.values())[:num_vehicles]

    return final_routes


# -------------------------------
# Example Usage
# -------------------------------

distance_matrix = [
    [0, 2, 9, 10, 7, 3, 8],
    [2, 0, 6, 4, 3, 5, 7],
    [9, 6, 0, 8, 5, 6, 4],
    [10, 4, 8, 0, 6, 7, 3],
    [7, 3, 5, 6, 0, 4, 5],
    [3, 5, 6, 7, 4, 0, 6],
    [8, 7, 4, 3, 5, 6, 0]
]

# Node 0 = depot
demands = [0, 1, 2, 1, 2, 1, 2]

vehicle_capacity = 5
num_vehicles = 3

routes = cvrp(distance_matrix, demands, vehicle_capacity, num_vehicles)


print("Optimized Routes:")
for i, route in enumerate(routes):
    print(f"Van {i+1}: {route}")


