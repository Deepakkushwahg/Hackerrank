n=int(input())
m=[]
s=[]
for i in range(0,n):
    name=input()
    score=float(input())
    s.append(score)
    s.append(name)
    m.append(s)
    s=[]
m.sort()
mini=m[0][0]
for i in range(len(m)):
    if(m[i][0]!=mini):
        mini=m[i][0]
        break
c=m.count(mini)
b=0
for i in range(len(m)):
    if(m[i][0]==mini):
        print(m[i][1])
    

