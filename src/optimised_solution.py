# 2-Opt: Optimised solution
from datasets import *
from greedy_solution import greedy

# Calculating the total distance of a given route
def route_distance(route, distance_matrix):
    dist = 0
    for i in range(len(route) - 1):
        first = route[i]
        second = route[i+1]

        two_dist = distance_matrix[first][second]
        dist += two_dist

    return dist
            

# Two-Opt Solution - optimising routes passed into the function according to distances in the distance matrix
def two_opt(routes, distance_matrix):
    optimised_routes = []

    # We work through each route looking to produce the optimal distance
    for r in range(len(routes)):
        best_route = routes[r]
        improved = True

        # The loop stays true until distance reduction is no longer possible, i.e Reversing the middle edges no longer does anything
        while improved:
            improved = False
            for i in range(1, len(best_route)-1):
                for j in range(i+1, len(best_route)-1):
                    new_route = best_route[:i] + best_route[i:j+1][::-1] + best_route[j+1:]  # Reverse the order of the nodes in between to check for distance reduction

                    # Check if reverse reduced overall route distance, if so then we stay in the loop and keep reversing until there is no change in distance 
                    if route_distance(new_route, distance_matrix) < route_distance(best_route, distance_matrix):
                        best_route = new_route
                        improved = True

        optimised_routes.append(best_route)

    return optimised_routes


distance_matrix = [ 
    [0,3,5,4,6,7,8],
    [3,0,2,6,4,5,7],
    [5,2,0,3,5,6,4],
    [4,6,3,0,2,5,6],
    [6,4,5,2,0,3,4],
    [7,5,6,5,3,0,2],
    [8,7,4,6,4,2,0]]

demands = [0,2,3,1,4,2,3]
n_vans = 3
max_cap = 5

# We now calculate the distances (naive and optimal) to check for improvements
# We take the routes of our naive attempt as these are the ones we want to optimise (i.e Reduce the distance)
routes, naive_distance = greedy(distance_matrix, demands, n_vans, max_cap)


optimal_routes = two_opt(routes, distance_matrix)
print(optimal_routes)

optimal_distance = 0

for i in range(len(optimal_routes)):
    dist = route_distance(optimal_routes[i], distance_matrix)
    optimal_distance += dist

print(f"Total greedy distance: {naive_distance}, Total optimal distance:{optimal_distance}")

