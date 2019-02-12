vec = []
import queue
import networkx as nw
import AC_1 as ac1
import AC_2 as ac2
import AC_3 as ac3
import AC_4 as ac4

lim = 11

if __name__ == '__main__':
    constraints = {}
    g = nw.gnm_random_graph(3, 0, False)
    domain = [[0 for x in range(3)] for y in range(3)]

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 2)


    print(g.edges)

    domain[0][0] = 1
    domain[0][1] = 2
    domain[0][2] = 3

    domain[1][0] = 0
    domain[1][1] = 4
    domain[1][2] = 5

    domain[2][0] = 2
    domain[2][1] = 5
    domain[2][2] = 6
    constraints[(0, 1)] = 0
    constraints[(1, 2)] = 4
    constraints[(0, 2)] = 6

    constraints[(1, 0)] = 0+lim
    constraints[(2, 1)] = 4+lim
    constraints[(2, 0)] = 6+lim

    print(ac4.AC4(g, constraints, domain, 3, 3, 3))
    print(domain)

