n1=int(input())
lst1=list(map(int, input().split()))
n2=int(input())
lst2=list(map(int, input().split()))
st1=set(lst1)
st2=set(lst2)
x=st1.difference(st2)
y=st2.difference(st1)
st=x.union(y)
lst=list(st)
lst.sort()
for i in lst:
    print(i)