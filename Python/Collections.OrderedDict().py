n=int(input())
ls=[]
lst=[]
for i in range(n):
    st=input().split()
    ls.append(st[0:len(st)-1])
    lst.append(st[-1])
for i in range(len(ls)):
    x=ls.count(ls[i])
    lst[i]=x*int(lst[i])
dct={}
for i in range(len(ls)):
    dct.update({tuple(ls[i]):lst[i]})
lst=list(dct)
ls=list(dct.values())
for i in range(len(lst)):
    lst[i]=list(lst[i])
    lst[i].append(ls[i])
for i in lst:
    print(*i)
