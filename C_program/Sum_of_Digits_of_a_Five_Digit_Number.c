#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int n, sum, a, b, c, d, e;
    scanf("%d", &n);
    a = n/10000;
    b = (n%10000)/1000;
    c = (n%1000)/100;
    d = (n%100)/10;
    e = n%10;
    sum = a+b+c+d+e;
    printf("%d", sum);
    return 0;
}
