t = int(input())
for i in range(t):
    n = int(input())
    set_A = set(map(int, input().split()))
    m = int(input())
    set_B = set(map(int, input().split()))
    print(set_A.issubset(set_B))
