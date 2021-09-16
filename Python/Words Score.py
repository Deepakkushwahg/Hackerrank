def score_words(words):
    s=0
    for i in words:
        c=0
        for j in i:
            if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='y'):
                c+=1
        if(c%2==0):
            p=2
        else:
            p=1
        s+=p
    return s    
