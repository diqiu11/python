#include<stdio.h>  

int main()
{
	int today=6;
	int day[7];
	long long N;
	scanf("%lld",&N);
	int i,sum=0;
	for(i=1;i<=7;i++)
	{
		sum += i*i;
		day[i%7]=(sum+today)%7;
	}
	printf("%d\n",day[N%7]);
    return 0; 
}  
