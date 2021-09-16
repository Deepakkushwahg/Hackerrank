#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main()
{
    int n,a,b,c,i,s[100];
    scanf("%d", &n);
    scanf("%d %d %d",&a,&b,&c);
    s[0]=a;
    s[1]=b;
    s[2]=c;
    s[3]=a+b+c;
    for(i=4;i<=n-1;i++)
    {
        s[i]=s[i-1]+s[i-2]+s[i-3];
    }
    printf("%d", s[i-1]);
    return 0;
}
