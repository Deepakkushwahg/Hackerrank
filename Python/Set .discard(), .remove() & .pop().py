n = int(input())
lst=set(map(int, input().split()))
N=int(input())
for i in range(N):
    st=list(input().split())
    if(st[0]=='pop'):
        lst.pop()
    elif(st[0]=='remove'):
        lst.remove(int(st[1]))
    elif(st[0]=='discard'):
        lst.discard(int(st[1]))
print(sum(lst))
