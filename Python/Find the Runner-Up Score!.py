n=int(input())
A=list(map(int, input().split(' ')))
A.sort(reverse=True)
max=A[0]
for i in A:
    if(max!=i):
        print(i)
        break
