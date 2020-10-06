#include <stdio.h>

int main(void)
{
	int g;
	int p = 0;
	
	for(g =2100000000 ; g >= 0; g--)
	{
		if(g % 2 == 0 && g % 3 == 0)
		{
			printf ("%d \n", g); 
			p = p + 1;
		}
	}
	printf ("총 개수는 %d 입니다 \n", p);
	
	return 0;
}                                                                                                           
