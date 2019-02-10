import queue
import constraints

def revise(xi, xj, constraint, domain):
    revised = False
    temp = []
    for i in domain[xi]:
        temp.append(i)

    for x in temp:
        single = False
        for y in domain[xj]:
            if(constraints.satisfy(x, y, constraint) == True):
                single = True

        if(single == False):
            domain[xi].remove(x)
            revised = True
        if(len(domain[xi]) == 0):
            break

    return revised

def AC3(g, constraints, domain, node, edge, domainSize):
    q = queue.Queue()

    for i in g.edges:
        q.put([i, constraints[i]])

    for i in g.edges:
        temp = (i[1], i[0])
        q.put([temp, constraints[temp]])

    while q.empty() is False:
        top = q.get()
        xi = top[0][0]
        xj = top[0][1]
        #print(top)
        constraint = top[1]
        if(revise(xi, xj, constraint, domain) == True):
            if(len(domain[xi]) == 0):
                return False
            for k in g.edges:
                if(k[0] == xi and k[1] != xj):
                    q.put([(k[1], k[0]), constraints[k]])
                elif(k[1]==xi and k[0] != xj):
                    q.put([(k[0], k[1]), constraints[k]])



    return True