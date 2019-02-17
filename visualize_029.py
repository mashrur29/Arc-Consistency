import numpy
import random
import networkx as nw
import matplotlib.pyplot as plt
from copy import deepcopy
from main_029 import executeAC1, executeAC2, executeAC3, executeAC4

lim = 11


def randInt(l, r):
    return random.randint(l, r)


def generateCSP(node, domainSiz):
    mini = node
    maxi = (node * (node + 1)) // 2
    edge = random.randint(mini, maxi)
    domainSize = domainSiz

    constraints = {}
    domain = [[0 for x in range(domainSize)] for y in range(node)]  # node x domainSize size list

    g = nw.gnm_random_graph(node, edge, False)

    for i in g.edges:
        constraints[i] = random.randint(0, 10)
        constraints[(i[1], i[0])] = constraints[i] + lim

    for i in range(node):
        for j in range(domainSize):
            domain[i][j] = randInt(1, 100)

    return (g, constraints, domain, edge, domainSize)


def visualize_nodes(domainSiz):
    xAc1 = []
    yAc1 = []
    xAc2 = []
    yAc2 = []
    xAc3 = []
    yAc3 = []
    xAc4 = []
    yAc4 = []

    for node in range(1, 101, 20):
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
            csp = generateCSP(node, domainSiz)
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
    #plt.savefig('node_variable_sized_domain.png')
    plt.show()


def visualize_edge(domainSz):
    xAc1 = []
    yAc1 = []
    xAc2 = []
    yAc2 = []
    xAc3 = []
    yAc3 = []
    xAc4 = []
    yAc4 = []

    xAc1.append(0)
    xAc2.append(0)
    xAc3.append(0)
    xAc4.append(0)

    yAc1.append(0)
    yAc2.append(0)
    yAc3.append(0)
    yAc4.append(0)

    for edge in range(0, 510, 100):
        print(edge)
        xAc1.append(edge)
        xAc2.append(edge)
        xAc3.append(edge)
        xAc4.append(edge)

        timeAc1 = 0
        timeAc2 = 0
        timeAc3 = 0
        timeAc4 = 0
        domainSize = domainSz
        node = 100

        for p in range(10):
            constraints = {}
            domain = [[0 for x in range(domainSize)] for y in range(node)]  # node x domainSize size list

            g = nw.gnm_random_graph(node, edge, False)

            for i in g.edges:
                constraints[i] = random.randint(0, 10)
                constraints[(i[1], i[0])] = constraints[i] + lim

            for i in range(node):
                for j in range(domainSize):
                    domain[i][j] = randInt(1, 100)


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
    plt.xlabel('Number of Edge')
    plt.ylabel('Performance (msec)')
    plt.title('Comparison of Arc Consistency Algorithm')
    plt.suptitle('@mashrur')
    plt.legend(loc='upper left')
    plt.savefig('edge_small_domain.png')
    plt.show()


def visualize_density(sz):
    xAc1 = []
    yAc1 = []
    xAc2 = []
    yAc2 = []
    xAc3 = []
    yAc3 = []
    xAc4 = []
    yAc4 = []
    node = 100

    for density in numpy.arange(0.1, 1.1, 0.3):
        xAc1.append(density)
        xAc2.append(density)
        xAc3.append(density)
        xAc4.append(density)

        timeAc1 = 0
        timeAc2 = 0
        timeAc3 = 0
        timeAc4 = 0
        domainSize = sz
        constraints = {}
        domain = [[0 for x in range(domainSize)] for y in range(node)]  # node x domainSize size list
        edge = (density*(node*(node-1)))//2
        edge = int(edge)
        print('lol', density, edge)
        g = nw.gnm_random_graph(node, edge, False)

        for i in g.edges:
            constraints[i] = random.randint(0, 10)
            constraints[(i[1], i[0])] = constraints[i] + lim

        for i in range(node):
            for j in range(domainSize):
                domain[i][j] = randInt(-1100, 1100)

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
    plt.xlabel('Graph Density')
    plt.ylabel('Performance (msec)')
    plt.title('Comparison of Arc Consistency Algorithm')
    plt.suptitle('@mashrur')
    plt.legend(loc='upper left')
    plt.savefig('density_large_domain.png')
    plt.show()

def visualize_domainReduction(domainSiz):
    xAc1 = []
    yAc1 = []
    xAc2 = []
    yAc2 = []
    xAc3 = []
    yAc3 = []
    xAc4 = []
    yAc4 = []

    for node in range(1, 101, 20):
        print(node)
        xAc1.append(node)
        xAc2.append(node)
        xAc3.append(node)
        xAc4.append(node)

        csp = generateCSP(node, domainSiz)
        g = csp[0]
        constraints = csp[1]
        domain = csp[2]
        edge = csp[3]
        domainSize = csp[4]
        initSizeAC1 = node*domainSize
        initSizeAC2 = node*domainSize
        initSizeAC3 = node*domainSize
        initSizeAC4 = node*domainSize
        finalSizeAC1 = 0
        finalSizeAC2 = 0
        finalSizeAC3 = 0
        finalSizeAC4 = 0

        domain1 = deepcopy(domain)
        domain2 = deepcopy(domain)
        domain3 = deepcopy(domain)
        domain4 = deepcopy(domain)
        executeAC1(node, edge, domainSize, deepcopy(g), deepcopy(constraints), domain1)
        executeAC2(node, edge, domainSize, deepcopy(g), deepcopy(constraints), domain2)
        executeAC3(node, edge, domainSize, deepcopy(g), deepcopy(constraints), domain3)
        executeAC4(node, edge, domainSize, deepcopy(g), deepcopy(constraints), domain4)
        for p in range(node):
            finalSizeAC1 += len(domain1[p])
            finalSizeAC2 += len(domain2[p])
            finalSizeAC3 += len(domain3[p])
            finalSizeAC4 += len(domain4[p])

        sizeAc1 = abs((finalSizeAC1-initSizeAC1)/initSizeAC1)
        sizeAc2 = abs((finalSizeAC2-initSizeAC2)/initSizeAC2)
        sizeAc3 = abs((finalSizeAC3-initSizeAC3)/initSizeAC3)
        sizeAc4 = abs((finalSizeAC4-initSizeAC4)/initSizeAC4)

        print('lol', sizeAc1, sizeAc2, sizeAc3, sizeAc4)
        yAc1.append(sizeAc1)
        yAc2.append(sizeAc2)
        yAc3.append(sizeAc3)
        yAc4.append(sizeAc4)

    plt.plot(xAc1, yAc1, color='g', label='AC 1')
    plt.plot(xAc2, yAc2, color='b', label='AC 2')
    plt.plot(xAc3, yAc3, color='r', label='AC 3')
    plt.plot(xAc4, yAc4, color='orange', label='AC 4')
    plt.xlabel('Number of Node')
    plt.ylabel('Domain Reduction')
    plt.title('Comparison of Arc Consistency Algorithm')
    plt.suptitle('@mashrur')
    plt.legend(loc='upper left')
    plt.savefig('node_domain_reduction.png')
    plt.show()