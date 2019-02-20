import random
import AC_1_029 as ac1
import AC_2_029 as ac2
import AC_3_029 as ac3
import AC_4_029 as ac4
import time
import visualize_029 as vis

lim = 11
cnt1 = None
cnt2 = None
cnt3 = None
cnt4 = None


def randInt(l, r):
    return random.randint(l, r)


def executeAC1(node, edge, domainSize, g, constraints, domain):
    global cnt1
    start_time = time.time()
    ac1.AC1(g, constraints, domain, node, edge, domainSize)
    cnt1 = ac1.cnt
    return ((time.time() - start_time) * 1000)


def executeAC2(node, edge, domainSize, g, constraints, domain):
    global cnt2
    start_time = time.time()
    ac2.AC2(g, constraints, domain, node, edge, domainSize)
    cnt2 = ac2.cnt
    return ((time.time() - start_time) * 1000)


def executeAC3(node, edge, domainSize, g, constraints, domain):
    global cnt3
    start_time = time.time()
    ac3.AC3(g, constraints, domain, node, edge, domainSize)
    cnt3 = ac3.cnt
    return ((time.time() - start_time) * 1000)


def executeAC4(node, edge, domainSize, g, constraints, domain):
    global cnt4
    start_time = time.time()
    ac4.AC4(g, constraints, domain, node, edge, domainSize)
    cnt4 = ac4.cnt
    return ((time.time() - start_time) * 1000)


if __name__ == '__main__':
    vis.visualize_nodes(20)
    # vis.visualize_density(100)
    # vis.visualize_edge(20)
    # vis.visualize_domainReduction(30)
    # vis.visualize_isSatNode(30)
    # vis.visualize_isSatEdge(100)
    print('---- DONE ----')
