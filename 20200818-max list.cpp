#include <stdio.h>

int main(void)
{
	int a[5] = {67, 78, 32, 54, 0};
	
	int max = a[0];
	
	for (int i = 1; i < 5; i++)
	{
		if (max < a[i])
		{
			max = a[i];
		}
	}
	
	printf ("%d \n", max);
	
	return 0;
}
