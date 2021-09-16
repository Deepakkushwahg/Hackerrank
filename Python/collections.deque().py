n=int(input())
lst=[]
for i in range(n):
    st=list(input().split())
    if(st[0]=='append'):
        lst.append(int(st[1]))
    elif(st[0]=='appendleft'):
        lst.insert(0,int(st[1]))
    elif(st[0]=='pop'):
        lst.pop()
    elif(st[0]=='popleft'):
        lst.pop(0)
for i in lst:
    print(i,end=' ')
        
