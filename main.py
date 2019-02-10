import random
import networkx as nw
import AC_1 as ac1
import AC_2 as ac2
import AC_3 as ac3
import time
import matplotlib.pyplot as plt


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
    ac3.AC3(g, constraints, domain, node, edge, domainSize)
    #print('Execution Time: ', ((time.time() - start_time) * 1000), 'sec')
    return ((time.time() - start_time) * 1000)


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
    ac1.AC1(g, constraints, domain, node, edge, domainSize)
    return ((time.time() - start_time) * 1000)
    #print('Execution Time: ', ((time.time() - start_time) * 1000), 'sec')

def executeAC2(node, edge, domainSize):
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
    ac2.AC2(g, constraints, domain, node, edge, domainSize)
    #print('Execution Time: ', ((time.time() - start_time) * 1000), 'sec')
    return ((time.time() - start_time) * 1000)

def visualize():
    xAc1 = []
    yAc1 = []

    for node in range(1, 200):
        print(node)
        xAc1.append(node)
        mini = node
        maxi = (node*(node+1))//2
        yAc1.append(executeAC1(node, random.randint(mini, maxi), 20))

    xAc2 = []
    yAc2 = []
    for node in range(1, 200):
        xAc2.append(node)
        mini = node
        maxi = (node*(node+1))//2
        print(mini, maxi)
        yAc2.append(executeAC2(node, random.randint(mini, maxi), 20))

    xAc3 = []
    yAc3 = []
    for node in range(1, 200):
        xAc3.append(node)
        mini = node
        maxi = (node * (node + 1)) // 2
        print(mini, maxi)
        yAc3.append(executeAC3(node, random.randint(mini, maxi), 20))

    plt.plot(xAc1, yAc1, color='g', label='AC 1')
    plt.plot(xAc2, yAc2, color='b', label='AC 2')
    plt.plot(xAc3, yAc3, color='r', label='AC 3')
    plt.xlabel('Number of Node')
    plt.ylabel('Performance (sec)')
    plt.title('Comparison of Arc Consistency Algorithm')
    plt.suptitle('@mashrur')
    plt.legend(loc='upper left')
    plt.savefig('foo.png')
    plt.show()

if __name__ == '__main__':
    visualize()
    print(executeAC2(30, 100, 100))

