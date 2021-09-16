n, m=map(int, input().split())
if(n%2!=0 and m==3*n and n>0):
    l=0
    for i in range(1,(m-3)//2,3):
        for j in range(i,(m-3)//2+1):
            print("-",end='')
        for k in range(1,i+1-l):
            print(".|.",end='')
        l+=1
        for j in range(i,(m-3)//2+1):
            print("-",end='')
        print()
    for i in range(m//2-3):
        print("-",end='')
    print("WELCOME",end='')
    for i in range(m//2-3):
        print("-",end='')
    print()
    for i in range(1,n//2+1):
        for k in range(1,i*3+1):
            print("-",end='')
        for j in range(i,n//2+1):
            print(".|.",end='')
        for j in range(i,n//2):
            print(".|.",end='')
        for k in range(1,i*3+1):
            print("-",end='')
        print()
        
