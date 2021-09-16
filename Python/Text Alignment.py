n=int(input())
if(n%2!=0 and n<50 and n>0):
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ",end='')
        for k in range(1,i+1):
            print("H",end='')
        for k in range(1,i):
            print("H",end='')
        print()
    k=0
    while(k<n+1):
        for i in range(n//2):
            print(" ",end='')
        for i in range(1,n+1):
            print("H",end='')
        for i in range(3*n):
            print(" ",end='')
        for i in range(1,n+1):
            print("H",end='')
        print()
        k+=1
    k=0
    while(k<n//2+1):
        for i in range(n//2):
            print(" ",end='')
        for i in range(5*n):
            print("H",end='')
        print()
        k+=1
    k=0
    while(k<n+1):
        for i in range(n//2):
            print(" ",end='')
        for i in range(1,n+1):
            print("H",end='')
        for i in range(3*n):
            print(" ",end='')
        for i in range(1,n+1):
            print("H",end='')
        print()
        k+=1
    for i in range(1,n+1):
        for m in range(n//2):
            print(" ",end='')
        for l in range(4*n-n//2):
            print(" ",end='')
        for k in range(1,i):
            print(" ",end='')
        for j in range(i,n+1):
            print("H",end='')
        for j in range(i,n):
            print("H",end='')
        print()
        
    
    
    
    
    
