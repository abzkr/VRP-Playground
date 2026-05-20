from datasets import *


def greedy(distance_matrix, demands, n_vans, max_cap):
    
    

    # Route Matrix
    routes= []

    for i in range(n_vans):
        routes.append([])
        routes[i].append(0)


    # Total distance travelled across all vehicles, this is what we want to reduce
    total_distance = 0

    #Set of all visited nodes, a node needs to be visted only once
    visited = set()

    # Iterate through each vans journey
    for i in range(n_vans):
        
        vehicle_cap = max_cap
        current_pos = 0

        # While there are still valid moves, move to that node and check for more valid moves around that node
        # If not, then terminate, move onto the next vehicle
        while True:

            
            # We take the sub-list of the surrounding nodes of our current position         
            current_pos_dist = distance_matrix[current_pos]
            lowest_cost = float ('inf') # infinity  bigger than all elements so will be replaced by the first element in the list (for comparative logic)
            new_pos = -1
            

            for z in range(len(current_pos_dist)):
                if z == current_pos: 
                    continue
                elif z == 0:  # Depot doesnt count as a node
                    continue
                elif demands[z] > vehicle_cap:
                    continue
                elif z in visited:
                    continue
                elif lowest_cost <= current_pos_dist[z]:
                    continue
                else:
                    lowest_cost = current_pos_dist[z]
                    new_pos = z
                            
            
            #  new pos is updated, this indicates that we moved to a new position and can add that to the list of visited nodes
            if new_pos != -1: 
                visited.add(new_pos)
                print(f"Vehicle {i+1}, current_pos: {current_pos}, new_pos: {new_pos}, lowest_cost: {lowest_cost}, vehicle_cap: {vehicle_cap}")

                current_pos = new_pos
                vehicle_cap -= demands[new_pos]
                total_distance += lowest_cost

                routes[i].append(new_pos)
            else:
                print (f"Vehicle {i+1} has reached full capacity -> Returning to depot")
                break
        
        routes[i].append(0)

            

        # Add the distance from current position to the repo to the end of the journey    
        total_distance += distance_matrix[current_pos][0]
        

    print(f"Complete! Total distance travelled across all vehicles is {total_distance}")
    print(routes)

    
    return routes, total_distance




# Distance Matrix -> 0-6 points (0 = Depot/bakery, 1-6 = Customer-locations/Cafes)
distance_matrix = [ [0,3,5,4,6,7,8],
                    [3,0,2,6,4,5,7],
                    [5,2,0,3,5,6,4],
                    [4,6,3,0,2,5,6],
                    [6,4,5,2,0,3,4],
                    [7,5,6,5,3,0,2],
                    [8,7,4,6,4,2,0]]

demands = [0,2,3,1,4,2,3]
n_vans = 3
max_cap = 5

greedy(distance_matrix, demands, n_vans, max_cap)
