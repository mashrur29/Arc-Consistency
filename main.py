import random
import networkx as nw
import AC_1 as ac1
import AC_2 as ac2
import AC_3 as ac3
import AC_4 as ac4
import time
import matplotlib.pyplot as plt
from copy import deepcopy

lim = 11

def randInt():
    return random.randint(1, 100)


def executeAC1(node, edge, domainSize, g, constraints, domain):
    start_time = time.time()
    ac1.AC1(g, constraints, domain, node, edge, domainSize)
    return ((time.time() - start_time) * 1000)

def executeAC2(node, edge, domainSize, g, constraints, domain):
    start_time = time.time()
    ac2.AC2(g, constraints, domain, node, edge, domainSize)
    return ((time.time() - start_time) * 1000)

def executeAC3(node, edge, domainSize, g, constraints, domain):
    start_time = time.time()
    ac3.AC3(g, constraints, domain, node, edge, domainSize)
    return ((time.time() - start_time) * 1000)

def executeAC4(node, edge, domainSize, g, constraints, domain):
    start_time = time.time()
    ac4.AC4(g, constraints, domain, node, edge, domainSize)
    return ((time.time() - start_time) * 1000)

def generateCSP(node):
    mini = node
    maxi = (node * (node + 1)) // 2
    edge = random.randint(mini, maxi)
    domainSize = 100

    constraints = {}
    domain = [[0 for x in range(domainSize)] for y in range(node)]  # node x domainSize size list

    g = nw.gnm_random_graph(node, edge, False)

    for i in g.edges:
        constraints[i] = random.randint(0, 10)
        constraints[(i[1], i[0])] = constraints[i] + lim

    for i in range(node):
        for j in range(domainSize):
            domain[i][j] = randInt()

    return (g, constraints, domain, edge, domainSize)

def visualize_nodes():
    xAc1 = []
    yAc1 = []
    xAc2 = []
    yAc2 = []
    xAc3 = []
    yAc3 = []
    xAc4 = []
    yAc4 = []

    for node in range(1, 60, 10):
        print(node)
        xAc1.append(node)
        xAc2.append(node)
        xAc3.append(node)
        xAc4.append(node)
        timeAc1 = 0
        timeAc2 = 0
        timeAc3 = 0
        timeAc4 = 0


        for i in range(10):
            csp = generateCSP(node)
            g = csp[0]
            constraints = csp[1]
            domain = csp[2]
            edge = csp[3]
            domainSize = csp[4]
            timeAc1 += executeAC1(node, edge, domainSize, deepcopy(g), deepcopy(constraints), deepcopy(domain))
            timeAc2 += executeAC2(node, edge, domainSize, deepcopy(g), deepcopy(constraints), deepcopy(domain))
            timeAc3 += executeAC3(node, edge, domainSize, deepcopy(g), deepcopy(constraints), deepcopy(domain))
            timeAc4 += executeAC4(node, edge, domainSize, deepcopy(g), deepcopy(constraints), deepcopy(domain))

        timeAc1 /= 10
        timeAc2 /= 10
        timeAc3 /= 10
        timeAc4 /= 10
        yAc1.append(timeAc1)
        yAc2.append(timeAc2)
        yAc3.append(timeAc3)
        yAc4.append(timeAc4)


    plt.plot(xAc1, yAc1, color='g', label='AC 1')
    plt.plot(xAc2, yAc2, color='b', label='AC 2')
    plt.plot(xAc3, yAc3, color='r', label='AC 3')
    plt.plot(xAc4, yAc4, color='orange', label='AC 4')
    plt.xlabel('Number of Node')
    plt.ylabel('Performance (msec)')
    plt.title('Comparison of Arc Consistency Algorithm')
    plt.suptitle('@mashrur')
    plt.legend(loc='upper left')
    plt.savefig('foo_node.png')
    plt.show()

def visualize_edge():
    xAc1 = []
    yAc1 = []
    xAc2 = []
    yAc2 = []
    xAc3 = []
    yAc3 = []
    xAc4 = []
    yAc4 = []

    for edge in range(10, 51, 10):
        print(edge)
        xAc1.append(edge)
        xAc2.append(edge)
        xAc3.append(edge)
        xAc4.append(edge)

        timeAc1 = 0
        timeAc2 = 0
        timeAc3 = 0
        timeAc4 = 0
        domainSize = 100
        node = 10
        constraints = {}
        domain = [[0 for x in range(domainSize)] for y in range(node)]  # node x domainSize size list

        g = nw.gnm_random_graph(node, edge, False)

        for i in g.edges:
            constraints[i] = random.randint(0, 10)
            constraints[(i[1], i[0])] = constraints[i] + lim

        for i in range(node):
            for j in range(domainSize):
                domain[i][j] = randInt()

        timeAc1 += executeAC1(node, edge, domainSize, deepcopy(g), deepcopy(constraints), deepcopy(domain))
        timeAc2 += executeAC2(node, edge, domainSize, deepcopy(g), deepcopy(constraints), deepcopy(domain))
        timeAc3 += executeAC3(node, edge, domainSize, deepcopy(g), deepcopy(constraints), deepcopy(domain))
        timeAc4 += executeAC4(node, edge, domainSize, deepcopy(g), deepcopy(constraints), deepcopy(domain))

        yAc1.append(timeAc1)
        yAc2.append(timeAc2)
        yAc3.append(timeAc3)
        yAc4.append(timeAc4)


    plt.plot(xAc1, yAc1, color='g', label='AC 1')
    plt.plot(xAc2, yAc2, color='b', label='AC 2')
    plt.plot(xAc3, yAc3, color='r', label='AC 3')
    plt.plot(xAc4, yAc4, color='orange', label='AC 4')
    plt.xlabel('Number of Edge')
    plt.ylabel('Performance (msec)')
    plt.title('Comparison of Arc Consistency Algorithm')
    plt.suptitle('@mashrur')
    plt.legend(loc='upper left')
    plt.savefig('foo_edge.png')
    plt.show()

if __name__ == '__main__':
    #visualize_nodes()
    visualize_edge()

