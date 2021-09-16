#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char a, b[50],c[50];
    scanf("%c", &a);
    scanf("%s\n", &b);
    scanf("%[^\n]*s", &c);
    printf("%c\n", a);
    printf("%s\n", b);
    printf("%s", c);
   
    return 0;
}
