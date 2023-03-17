
# ASSIGNMENT 3: GENETIC ALGORITHM

from geneticAlgorithm import Genetic_Algorithm

boxes = [(1, 20, 6),
         (2, 30, 5),
         (3, 60, 8),
         (4, 90, 7),
         (5, 50, 6),
         (6, 70, 9),
         (7, 30, 4),
         (8, 30, 5),
         (9, 70, 4),
         (10, 20, 9),
         (11, 20, 2),
         (12, 60, 1)] # tuple: number, weight, value

backpack_size = 250
limit = 100 # convergence limit
mutation_probability = 0.05 # 5% chance of single mutation
population_size = 100

search = Genetic_Algorithm(backpack_size, limit, mutation_probability, boxes)
# create population of individuals with given population size
population = search.create_population(population_size)
# find best solution to problem until convergence
solution = search.run(population)
print("Found this solution after", solution[2], "generations:")
for i in range(len(solution[0])):
    if (solution[0][i]):
        print("Include box", boxes[i][0])
print("Total value:", solution[1])