def vacuumCleaner(floor):
    m = len(floor)
    n = len(floor[0])
    for i in range(m):
          for j in range(n):
               if(floor[i][j] == 1):
                    print("ROOM ",i,j,"  DIRTY")
                    floor[i][j] = 0
                    print("ROOM ",i,j," CLEANED")
               else:
                    print("ROOM  ",i,j," CLEAN")
    print("ALL ROOMS CLEANED")

floor = [[1, 1, 0],
           [0, 0, 0],
           [0, 1, 1],
           [0, 1, 0]]
vacuumCleaner(floor)
