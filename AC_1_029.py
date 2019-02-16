import queue
import constraints_029

def revise(xi, xj, constraint, domain):
    revised = False
    temp = []
    for i in domain[xi]:
        temp.append(i)

    #print('Here ', xi, ' ', xj)
    for x in temp:
        single = False
        for y in domain[xj]:
            if(constraints_029.satisfy(x, y, constraint) == True):
                single = True
            #print('checking: ', x, ' ', y, ' ', constraints.satisfy(x, y, constraint))

        #print('Domain ', x, ' ', domain[xi])
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

def AC1(g, constraints, domain, node, edge, domainSize):
    q = []

    for i in g.edges:
        q.append([i, constraints[i]])

    for i in g.edges:
        temp = (i[1], i[0])
        q.append([temp, constraints[temp]])

    while True:
        change = False

        for it in q:
            xi = it[0][0]
            xj = it[0][1]
            constraint = it[1]
            #print(xi, xj, constraint)
            if(revise(xi, xj, constraint, domain) == True):
                change = True

        if change == False:
            break

    return solutionExists(domain)