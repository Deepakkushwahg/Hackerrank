#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int i, d[128]={};
    char a[1000];
    scanf("%[^\n]", a);
    for(i=0;a[i]!='\0';i++)
        d[a[i]]++;
    for(i=48;i<=57;i++)
        printf("%d ", d[i]);
    
    return 0;
}
