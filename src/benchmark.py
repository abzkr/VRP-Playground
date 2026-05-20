import time
from datasets import *
import matplotlib.pyplot as plt
from greedy_solution import greedy
from optimised_solution import two_opt, route_distance
from ai_solution import cvrp, calculate_savings


# Naive Solution (Greedy) Benchmark -> we are taking both the time and distance here, as the algo returns both
start_greedy = time.time()
greedy_routes, greedy_distance = greedy(distance_matrix, demands, n_vans, max_cap)
end_greedy = time.time()
greedy_time = end_greedy - start_greedy




# AI Generated Solution time benchmark
start_ai = time.time()
ai_routes = cvrp(distance_matrix, demands, max_cap, n_vans)
end_ai = time.time()
ai_time = end_ai - start_ai

# AI Generated Solution distance benchmark
ai_sol_distance = 0
for i in range(len(ai_routes)):
    ai_sol_distance += route_distance(ai_routes[i], distance_matrix)  





# Optmised Solution (2-opt) time benchmark
start_optimal = time.time()
optimal_routes = two_opt(greedy_routes, distance_matrix)   # We use the results from our naive and optimise the routes returned
end_optimal = time.time()
optimal_time = end_optimal - start_optimal


# Optimised distance benchmark
optimal_distance = 0
for i in range(len(optimal_routes)):
    dist = route_distance(optimal_routes[i], distance_matrix)
    optimal_distance += dist




# Benchmark Outputs
print(f"Greedy Solution Time: {greedy_time}, AI Solution Time: {ai_time} and Optimal Solution Time: {optimal_time}")
print(f"Greedy Solution Distance: {greedy_distance}, AI Solution Time: {ai_sol_distance} and Optimal Solution Distance: {optimal_distance}")



# Visual outputs

# Time Bar Graph
solutions = ['Naive', 'AI-gen', 'Optimised']
time_values = [greedy_time, ai_time, optimal_time]

plt.bar(solutions, time_values)
plt.xlabel('Solutions/Algorithms')
plt.ylabel('Time')
plt.title('Time For Algorithm Completion')

plt.show()

# Distance Bar Graph
distance_values = [greedy_distance, ai_sol_distance, optimal_distance]

plt.bar(solutions, distance_values)
plt.xlabel('Solutions/Algorithms')
plt.ylabel('Total Distance')
plt.title('Distance Travelled Using Each Algorithm')

plt.show()


'''
In order to do our final benchmark of comparing total distance as number of nodes increase, we
need to run the algorithms a few more time and pass in different datasets in the arguments at each run.
'''

# 9 total nodes
greedy_routes_1, greedy_distance_1 = greedy(distance_matrix_1, demands_1, n_vans_1, max_cap_1)   
optimal_routes_1 = two_opt(greedy_routes_1, distance_matrix_1)

ai_routes_1 = cvrp(distance_matrix_1, demands_1, max_cap_1, n_vans_1)
ai_sol_distance_1= 0
for i in range(len(ai_routes_1)):
    ai_sol_distance_1 += route_distance(ai_routes_1[i], distance_matrix_1) 

optimal_distance_1 = 0
for i in range(len(optimal_routes_1)):
    dist = route_distance(optimal_routes_1[i], distance_matrix_1)
    optimal_distance_1 += dist




# 10 total nodes
greedy_routes_2, greedy_distance_2 = greedy(distance_matrix_2, demands_2, n_vans_2, max_cap_2)   
optimal_routes_2 = two_opt(greedy_routes_2, distance_matrix_2)

ai_routes_2 = cvrp(distance_matrix_2, demands_2, max_cap_2, n_vans_2)
ai_sol_distance_2= 0
for i in range(len(ai_routes_2)):
    ai_sol_distance_2 += route_distance(ai_routes_2[i], distance_matrix_2) 

optimal_distance_2 = 0
for i in range(len(optimal_routes_2)):
    dist = route_distance(optimal_routes_2[i], distance_matrix_2)
    optimal_distance_2 += dist




# 12 total nodes
greedy_routes_3, greedy_distance_3 = greedy(distance_matrix_3, demands_3, n_vans_3, max_cap_3)   
optimal_routes_3 = two_opt(greedy_routes_3, distance_matrix_3)

ai_routes_3 = cvrp(distance_matrix_3, demands_3, max_cap_3, n_vans_3)
ai_sol_distance_3= 0
for i in range(len(ai_routes_3)):
    ai_sol_distance_3 += route_distance(ai_routes_3[i], distance_matrix_3) 

optimal_distance_3 = 0
for i in range(len(optimal_routes_3)):
    dist = route_distance(optimal_routes_3[i], distance_matrix_3)
    optimal_distance_3 += dist



# 15 total nodes
greedy_routes_4, greedy_distance_4 = greedy(distance_matrix_4, demands_4, n_vans_4, max_cap_4)   
optimal_routes_4 = two_opt(greedy_routes_4, distance_matrix_4)

ai_routes_4 = cvrp(distance_matrix_4, demands_4, max_cap_4, n_vans_4)
ai_sol_distance_4= 0
for i in range(len(ai_routes_4)):
    ai_sol_distance_4 += route_distance(ai_routes_4[i], distance_matrix_4) 

optimal_distance_4 = 0
for i in range(len(optimal_routes_4)):
    dist = route_distance(optimal_routes_4[i], distance_matrix_4)
    optimal_distance_4 += dist







# Comparing distance travelled as number of nodes increases

# X
nodes = [7, 9, 10, 12, 15]

# Y
greedy_algo = [greedy_distance, greedy_distance_1, greedy_distance_2, greedy_distance_3, greedy_distance_4]
ai_gen_algo = [ai_sol_distance, ai_sol_distance_1, ai_sol_distance_2, ai_sol_distance_3,  ai_sol_distance_4]
two_opt_algo = [optimal_distance, optimal_distance_1, optimal_distance_2, optimal_distance_3,  optimal_distance_4]

# Plot each algo
plt.plot(nodes, greedy_algo, marker='o', label='Greedy (Naive)')
plt.plot(nodes, ai_gen_algo, marker='s', label='AI gen (CVRP)')
plt.plot(nodes, two_opt_algo, marker='^', label='Two-Opt (Optimised)')

# axis labels
plt.xlabel('Number of Nodes')
plt.ylabel('Total Distance')
plt.title('Algorithm Distance Comparison: Increasing number of nodes')

# Key
plt.legend()

plt.show()