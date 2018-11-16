import math
import random
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y, name = None):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        # inners = '{}: ({}, {})'.format(self.name, self.x, self.y)
        # return f"{inners}"
        return self.name

    def get_location(self):
        return self.x, self.y

class DNA:
    def __init__(self, strand):
        self.strand = strand
        self.fitness = calculate_fitness(strand)
    
    def __repr__(self):
        return '{' + f"{self.fitness} : {self.strand}" + '}'

def generate_random_locations(number_of_locations):
    locations = []
    for i in range(number_of_locations):
        locations.append(generate_random_location(str(i)))
    return locations

def generate_random_location(name =""):
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    return Node(x, y, name)

def generate_circle(num_points):
    locations = []
    for i in range(num_points):
        angle = (i/num_points)*math.pi*2
        x = math.cos(angle)*20
        y = math.sin(angle)*20
        locations.append(Node(int(x), int(y), str(i)))
    return locations

### START ###

population_size = 10
num_locations = 15

locations = generate_circle(num_locations)
print('Locations: ', locations)

def create_population(size, locations):
    pop = []
    for i in range(size):
        dna = create_one_dna_from(locations)
        # fitness = calculate_fitness(dna)
        # pop[fitness] = dna
        pop.append(dna)
    return pop

def create_one_dna_from(locations):
    strand = []
    locs = locations[:]
    
    while locs:
        random_location = locs.pop(random.randint(0, len(locs) - 1))
        strand.append(random_location)
    
    return DNA(strand)

def create_one_offspring(dna_1, dna_2):
    split_point_1 = generate_random_index_in_strand(dna_1)
    split_point_2 = generate_random_index_in_strand(dna_1)
    crossover = dna_1[min(split_point_1, split_point_2) : max(split_point_1, split_point_2)]

    for i in dna_2:
        if i not in crossover:
            crossover.append(i)

    return crossover

def generate_random_index_in_strand(dna):
    return random.randint(0, len(dna))

def calculate_fitness(dna):
    total_distance = 0
    
    for i in range(len(dna) - 1):
        two_nodes = dna[i:i+2]
        total_distance += distance_between_nodes(two_nodes[0], two_nodes[1])
    total_distance += distance_between_nodes(dna[-1], dna[0])

    return total_distance

def distance_between_nodes(node_1, node_2):
    return math.hypot(node_2.x - node_1.x, node_2.y - node_1.y)

def sort_population(pop):
    return sorted(pop, key=lambda node: node.fitness)

## GRAPHING

def generate_graph(locations, population):
    plt.clear()
    graph = nx.Graph()

    for location in locations:
        graph.add_node(location.name, pos=location.get_location())

    best_child = population[0]
    for i in range(len(best_child) - 1):
        s = best_child[i:i+2]
        graph.add_edge(str(s[0]), str(s[1]))
    graph.add_edge(str(best_child[-1]), str(best_child[0]))

    pos = nx.get_node_attributes(graph, "pos")
    nx.draw(graph, pos, with_labels=True)
    plt.show()

## HELPER
def pprint(d):
    print("[")
    for i in d:
        print(f"  {i}")
    print("]")

#####################################
# Create population
# Randomize population genes
#
# Create children
# Mutate children
# Fitness
# Sort
# Trim
#####################################

population = create_population(population_size, locations)
for dna in population:
    
pprint(population)
pprint(sort_population(population))
# pprint.pprint(population[sorted(population)[0]])
# for i in range(len(population)):
    # print('pop[', i ,']:', calculate_fitness(population[i]), "dna:", population[i])

# print(sorted(population))

# print('pop[2]:', population[1])
# generate_graph(locations, population)

# print('child 1: ', create_one_offspring(population[0], population[1]))
# print('child 2: ', create_one_offspring(population[1], population[0]))

