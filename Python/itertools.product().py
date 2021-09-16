lst1=list(map(int, input().split()))
lst2=list(map(int, input().split()))
lst=[]
ls=[]
for i in lst1:
    for j in lst2:
        ls.append(i)
        ls.append(j)
        lst.append(tuple(ls))
        ls=[]
for i in lst:
    print(i,end=' ')
