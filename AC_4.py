import queue
import constraints as cons
from copy import deepcopy


def revise(xi, xj, constraint, domain):
    revised = False
    temp = []
    for i in domain[xi]:
        temp.append(i)

    for x in temp:
        single = False
        for y in domain[xj]:
            if(cons.constraints.satisfy(x, y, constraint) == True):
                single = True

        if(single == False):
            domain[xi].remove(x)
            revised = True
        if(len(domain[xi]) == 0):
            break

    return revised


def solutionExists(domain):
    for i in range(len(domain)):
        if(len(domain[i]) == 0):
            return False

    return True

def AC4(g, constraints, domain, node, edge, domainSize):
    q = queue.Queue()
    s = {}
    counter = {}
    global i, j

    for i in range(len(domain)):
        for j in domain[i]:
            s[(i, j)] = []
            for k in range(node):
                counter[(i, j, k)] = 0

    arc = []
    for i in g.edges:
        arc.append(i)

    for i in g.edges:
        arc.append((i[1], i[0]))

    for i in arc:
        vi = i[0]
        vj = i[1]
        temp = []
        for i in domain[vi]:
            temp.append(i)


        for ai in temp:
            for aj in domain[vj]:
                if(cons.satisfy(ai, aj, constraints[(vi, vj)]) == True):
                    counter[(vi, ai, vj)] += 1
                    s[(vj, aj)].append((vi, ai))

            if (counter[(vi, ai, vj)] == 0):
                q.put((vi, ai))
                domain[vi].remove(ai)
            if(len(domain[vi]) == 0):
                return False


    while q.empty() is False:
        top = q.get()
        vj = top[0]
        aj = top[1]

        for k in s[top]:
            belongsTo = False
            vi = k[0]
            ai = k[1]

            if(len(domain[vi]) == 0):
                return False

            for i in domain[vi]:
                if(i == ai):
                    belongsTo = True
                    break
            if(belongsTo == True):
                counter[(vi, ai, vj)] -= 1
                if(counter[(vi, ai, vj)] == 0):
                    q.put((vi, ai))
                    domain[vi].remove(ai)


    return True