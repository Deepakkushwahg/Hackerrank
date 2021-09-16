n=int(input())
lst1=list(map(int, input().split()))
set1=set(lst1)
N=int(input())
for i in range(N):
    st=list(input().split())
    lst=set(list(map(int, input().split())))
    if(st[0]=='intersection_update'):
        set1.intersection_update(lst)
    elif(st[0]=='update'):
        set1.update(lst)
    elif(st[0]=='symmetric_difference_update'):
        set1.symmetric_difference_update(lst)
    elif(st[0]=='difference_update'):
        set1.difference_update(lst)
print(sum(set1))
