n, m=map(int, input().split())
lst=list(map(int, input().split()))
lst1=set(map(int, input().split()))
lst2=set(map(int, input().split()))
c1=c2=s=0
for i in lst:
    if(i in lst1):
        c1=1
    if(i in lst2):
        c2=1
    s+=c1-c2
    c1=c2=0
print(s)
