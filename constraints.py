lim = 11

def satisfy(a, b, constraint):
    ta = a
    tb = b
    if constraint > 10:
        constraint = constraint - lim
        ta = b
        tb = a

    if(constraint == 0 and ta < tb):
        return True
    elif(constraint == 1 and 4*ta>tb+1):
        return True
    elif(constraint == 2 and ta>=tb):
        return True
    elif(constraint==3 and tb<=2*ta):
        return True
    elif(constraint==4 and ta==tb):
        return True
    elif(constraint==5 and ta*2 >= tb):
        return True
    elif(constraint==6 and divmod(ta, tb)==1):
        return True
    elif(constraint==7 and ta!=tb):
        return True
    elif(constraint==8 and tb+ta>=7):
        return True
    elif(constraint==9 and ta>=2*tb+5):
        return True
    elif(constraint==10 and tb<=4*ta+6):
        return True
    else:
        return False