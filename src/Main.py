# Create population
# Randomize population genes

# Create children
# Mutate children
# Fitness
# Sort
# Trim

import math
import random
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y, name = ""):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        # return '{}: ({}, {})'.format(self.name, self.x, self.y)
        return self.name

    def get_location(self):
        return self.x, self.y


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

population_size = 5
num_locations = 15

locations = generate_circle(num_locations)
print('Locations: ', locations)

def create_population(size):
    pop = []
    # for i in range(size):
    #     if
    return pop

def create_one_dna_from(locations):
    dna = []
    

def create_offspring(parent_1, parent_2):
    pass







def generate_graph():
    graph = nx.Graph()

    for location in locations:
        graph.add_node(location.name, pos=location.get_location())

    pos = nx.get_node_attributes(graph, "pos")
    nx.draw(graph, pos, with_labels=True)
    plt.show()

generate_graph()