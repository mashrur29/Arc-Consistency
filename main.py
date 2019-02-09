import numpy as np
import random
import networkx as nw
import AC_3 as ac3
import time

lim = 11

def randInt():
    return random.randint(1, 100)

def executeAC3(node, edge, domainSize):
    constraints = {}
    domain = [[0 for x in range(domainSize)] for y in range(node)]  # node x domainSize size list

    g = nw.gnm_random_graph(node, edge, False)

    for i in g.edges:
        constraints[i] = random.randint(0, 10)
        constraints[(i[1], i[0])] = constraints[i] + lim


    for i in range(node):
        for j in range(domainSize):
            domain[i][j] = randInt()


    start_time = time.time()
    print(ac3.AC3(g, constraints, domain, node, edge, domainSize))
    print('Execution Time:')
    print((time.time() - start_time) * 1000)


def executeAC1(node, edge, domainSize):
    constraints = {}
    domain = [[0 for x in range(domainSize)] for y in range(node)]  # node x domainSize size list

    g = nw.gnm_random_graph(node, edge, False)

    for i in g.edges:
        constraints[i] = random.randint(0, 10)
        constraints[(i[1], i[0])] = constraints[i] + lim

    for i in range(node):
        for j in range(domainSize):
            domain[i][j] = randInt()

    start_time = time.time()
    print(ac3.AC3(g, constraints, domain, node, edge, domainSize))
    print('Execution Time:')
    print((time.time() - start_time) * 1000)

if __name__ == '__main__':
    executeAC3(30, 100, 100)

