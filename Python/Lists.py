n=int(input())
lst=[]
for i in range(n):
    l=input().split()
    if(l[0]=='insert'):
        lst.insert(int(l[1]),int(l[2]))
    elif(l[0]=='append'):
        lst.append(int(l[1]))
    elif(l[0]=='pop'):
        lst.pop()
    elif(l[0]=='print'):
        print(lst)
    elif(l[0]=='remove'):
        lst.remove(int(l[1]))
    elif(l[0]=='sort'):
        lst.sort()
    elif(l[0]=='reverse'):
        lst.reverse()
