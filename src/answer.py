def generate_population():
    population = []
    for i in range(16):
        binary = "{0:04b}".format(i)
        population.append([int(j) for j in list(binary)])
    return population

def constraint(current):
    x1, x2, x3, x4 = current

    return 0.5*x1+1.0*x2+1.5*x3+0.1*x4 <= 3.1 and \
        0.3*x1+0.8*x2+1.5*x3+0.4*x4 <= 2.5 and \
        0.2*x1+0.2*x2+0.3*x3+0.1*x4 <= 0.4

def fitness(current):
    x1, x2, x3, x4 = current

    return 0.2*x1+0.3*x2+0.5*x3+0.1*x4

pop = generate_population()
max_array = dict()

for i in pop:
    if constraint(i):
        max_array[str(i)] = fitness(i)


from pprint import pprint
pprint(max_array, indent=2)