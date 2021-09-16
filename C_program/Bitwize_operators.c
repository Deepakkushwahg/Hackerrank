#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int n, k, i, j, l=2, max1=0, max2=0, max3=0;
    scanf("%d %d", &n, &k);
    for(i=1;i<=k;i++)
    {
        for(j=l;j<=n;j++)
        {
            if(max1<(i&j) && (i&j)<k)
                max1=(i&j);
            else if(max1>=(i&j) && (i&j)<k) 
                max1=max1;
            if(max2<(i|j) && (i|j)<k)
                max2=(i|j);
            else if(max2>=(i|j) && (i|j)<k)
                max2=max2;
            if(max3<(i^j) && (i^j)<k)
                max3=(i^j);
            else if(max3>=(i^j) && (i^j)<k)
                max3=max3;
        }
        l++;
    }
    printf("%d\n%d\n%d", max1, max2, max3);
    return 0;
}
