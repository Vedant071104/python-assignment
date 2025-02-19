# Q.1
n=int(input("enter number of square you want"))
d1={e:e**2 for e in range(1,n+1)}
print(d1)

#Q.2)
d2={4:"ved",3:"vai",2:"rj",1:"dad"}
d3={}
for k in sorted(d2,reverse=True):
    d3[k]=d2[k]
    print(d3)
    

 
#Q.3)
p=[n for n in input("Enter player name seperated by comma").split(",")] 
player={}
for e in p:
    print("Total matches")
    matches=int(input())
    print("Total runs")
    runs=int(input())
    print("Total half centuries")
    hc=int(input())
    print("Total enturies")
    centuries=int(input())
    player[e]=(matches,runs,hc,centuries)
    print(player)
    
#Q.4