import random
import heapq

class Genetic_Algorithm:

    def __init__(self, backpack_size, limit, mutation, box_list):
        self.backpack_size = backpack_size
        self.limit = limit
        self.boxes = box_list
        self.mutation_probability = mutation

        self.cull_rate = 0.5 # 50% cull rate
        self.boxes_weight = 0 # total weight of all boxes
        self.boxes_value = 0 # total value of all boxes
        for box in self.boxes: # calculate total weight and value of boxes
            self.boxes_weight += box[1]
            self.boxes_value += box[2]
    

    def create_population(self, size):
        # create population of given size
        population = []
        for i in range(size):
            individual = []
            # fill individual genome with random true/false values corresponding to boxes; true if box is included in backpack, false if not
            for j in range(len(self.boxes)):
                individual.append(random.choice([True, False]))
            population.append(individual) # add individual to population
        return population


    def fitness_sort(self, population):
        # sort according to fitness, highest to lowest
        self.sorted_tuple = []
        for individual in population:
            heapq.heappush(self.sorted_tuple, self.get_fitness(individual))
        self.sorted_tuple.reverse()
        for i in range(len(population)):
            population[i] = self.sorted_tuple[i][1] # get individual from tuple
        # return population and highest fitness
        return population, self.sorted_tuple[i][0]
        

    def get_fitness(self, individual):
        total_value = 0
        total_weight = 0
        # get total weight and value of all boxes used in individual
        for i in range(len(individual)): 
            if (individual[i]):
                total_value += self.boxes[i][2]
                total_weight += self.boxes[i][1]
        fitness = total_value
        # if weight exceeds backpack size, penalize fitness
        if total_weight > self.backpack_size:
            fitness = 0
        return (fitness, individual)

    def cull(self, population):
        # take half of population with best fitness
        return population[:int(len(population)*self.cull_rate)]

    def single_mutation(self, individual):
        # occasionally change single gene in genome 
        i = random.randint(0, len(individual)-1)
        if random.randint(0, 100) < self.mutation_probability:
            # switch true/false value
            individual[i] = True if False else False
        return individual

    def crossover_mutation(self, first, second):
        # take section from first genome and section from second at random splice point to make new individual
        crosspoint = random.randint(1, len(first)-1)
        if (random.randint(0,1) == 0):
            return first[:crosspoint] + second[crosspoint:]
        else:
            return second[:crosspoint] + first[crosspoint:]
    
    def run(self, population):
        generations = 0
        best = [None, 0, 0] # best individual, best fitness, generation found
        converged = False
        while(not converged): 
            # sort population and find highest fitness value
            population, value = self.fitness_sort(population)
            # check if new best solution has been found
            if (value > best[1]):
                best[0] = population[0]
                best[1] = value
                best[2] = generations
            # improve over fitness of population each generation
            population = self.cull(population)
            size = len(population)
            # crossbreed random individuals in population, add back
            for i in range(size):
                first = population[random.randint(0, size-1)]
                second = population[random.randint(0, size-1)]
                child = self.crossover_mutation(first, second)
                child = self.single_mutation(child)
                population.append(child)
            generations += 1
            # if the best has not improved with many generations, the best solution has likely been found
            if generations > best[2] + self.limit:
                converged = True

        # return best solution individual, fitness, and generation found
        return tuple(best)
        


