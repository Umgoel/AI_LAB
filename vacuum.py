def vacuumCleaner(flr):
    n = len(flr)
    v = 0
    cost=0
    if(v==0):
        if(flr[v]==1):
            flr[v]=0
            cost+=1
            print("Cleaned room no. ",v)
            v=1
    if(v==1):
         if(flr[v]==1):
            flr[v]=0
            cost+=1
            print("Cleaned room no. ",v)
    print("total cost = ",cost)

flr = [1,1]
vacuumCleaner(flr)
