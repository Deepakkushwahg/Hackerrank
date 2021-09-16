#include<stdio.h>
#include<string.h>
#include<math.h>

int main()
{
    int a, b, *pa=&a, *pb=&b;
    scanf("%d\n%d", pa, pb);
    printf("%d\n", *pa+*pb);
    printf("%d", abs(*pa-*pb));
    return 0;
}
