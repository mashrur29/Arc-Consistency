import queue
import constraints_029

def revise(xi, xj, constraint, domain):
    revised = False
    temp = []
    for i in domain[xi]:
        temp.append(i)

    for x in temp:
        single = False
        for y in domain[xj]:
            if(constraints_029.satisfy(x, y, constraint) == True):
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

def AC2(g, constraints, domain, node, edge, domainSize):
    arcs = []
    node = len(domain)

    for i in g.edges:
        arcs.append(i)
    for i in g.edges:
        arcs.append((i[1], i[0]))

    for nod in range(node):
        q = queue.Queue()
        q1 = queue.Queue()

        for i in arcs:
            if(i[0]==nod and i[1]<nod):
                q.put([i, constraints[i]])

        for i in arcs:
            if(i[1]==nod and i[0]<nod):
                q1.put([i, constraints[i]])


        while q.empty() is False:
            while q.empty() is False:
                top = q.get()
                xi = top[0][0]
                xj = top[0][1]
                constraint = top[1]
                if(revise(xi, xj, constraint, domain) == True):
                    for k in arcs:
                        if(k[1]==xi and k[0] != xj and k[0]<=nod):
                            q.put([(k[0], k[1]), constraints[k]])

            while q1.empty() is False:
                q.put(q1.get())


    return solutionExists(domain)