#Vacuum cleaner problem
status = [1,1]
print(status)
cost = 0
for i in range(len(status)) :
    if status[i]==0:
        print ("Room ",i+1," clear")
        continue
    else:
        if(i>0):
            cost+=1
        print("Room ",i+1," dirty")
        status[i] = status[i]-1
        print("Room ",i+1," Cleared")
        cost+=1
print("cost = ",cost)
