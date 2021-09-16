#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char str1[1000], str2[1000];
    int i, c=0, j=0;
    scanf("%[^\n]", &str1);
    for(i=0;i<=strlen(str1)+1;i++)
    {
        c=0;
        if(str1[i]==' ' || str1[i]=='\0')
        {
            str2[j]='\0';
            c=1;
            j++;
        }
        else 
        {
            str2[j]=str1[i];
            j++;
        }
        if(c==1)
        {
            printf("%s\n", str2);
            j=0;
        }
            
    }
    return 0;
}
