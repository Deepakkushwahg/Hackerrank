def print_rangoli(size):
    if(size==1):
        print("a")
    else:
        l=2
        x=1
        for i in range(1,(size-1)*2+1,2):
            for j in range(i,(size-1)*2+1):
                print("-",end='')
            print(chr(97+size-1),end='')
            if(i==1):
                for j in range(1,size):
                    print("--",end='')
            else:
                for k in range(1,i-l+1):
                    print("-"+chr(97+size-1-k),end='')
                for j in range(97+size-x,97+size):
                    print("-"+chr(j),end='')
                for j in range(i,(size-1)*2+1):
                    print("-",end='')        
                x+=1
                l+=1
            print()
        l=97+size-1
        while(l>=97):
            print(chr(l)+"-",end='')
            l-=1
        l=98
        while(l<97+size-1):
            print(chr(l)+"-",end='')
            l+=1
        print(chr(97+size-1))
        for i in range(1,size):
            if(i==size-1):
                for j in range(1,size):
                    print("--",end='')
                print(chr(97+size-1),end='')
                for j in range(1,size):
                    print("--",end='')
            else:
                for k in range(1,i+1):
                    print("--",end='')
                for j in range(97+size-1,96+i,-1):
                    print(chr(j)+"-",end='')
                for j in range(98+i,97+size-1):
                    print(chr(j)+"-",end='')
                print(chr(97+size-1),end='')
                for k in range(1,i+1):
                    print("--",end='')
            print()
        

