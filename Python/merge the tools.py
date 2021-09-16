def merge_the_tools(string, k):
    lst=[]
    j=0
    n=len(string)//k
    for i in range(n):
        lst.append(string[j:j+k])
        j+=k
    for m in lst:
        print(''.join(list(dict.fromkeys(list(m)).keys())))


