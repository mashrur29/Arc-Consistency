import random
import networkx as nw
import AC_1 as ac1
import AC_2 as ac2
import AC_3 as ac3
import AC_4 as ac4
import time
import visualize as vis

lim = 11

def randInt(l, r):
    return random.randint(l, r)

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

if __name__ == '__main__':
    vis.visualize_density(100)
    #vis.visualize_edge()
    print('---- DONE ----')

