//karandeep Singh
//vitVellore 
#include <stdio.h>
#include <math.h>
void primefact(long n)
{
    long long m=0;
   
   while(n%2==0)
   {
       n=round(n/2);
       m=2;
   }
    
    for(long i=3; i<=round(sqrt(n)); i+=2)
    {
        while(round(n%i)==0)
        {
            if(i>m)
                m=i;
            n=round(n/i);
        }
        
    }
if (n > 2)
{
    if(n>m)
        m=n;
}
    printf("%d\n",m);

}
int main()
{
    int t;
    scanf("%d",&t);
    long long a[t];
    if(t>=1 && t<=10)
        for(long i=0;i<t;i++)
        {
            long long n;
            scanf("%d",&n);
            if(n>=10 && n<=10000000000)
                a[i]=n;
        }
        

for(long i=0;i<t;i++)
{
    primefact(a[i]);
}
    return 0;
}
