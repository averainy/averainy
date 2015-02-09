/*************************************************************************
	> File Name: test.c
	> Author: averainy
	> Mail: averainy@gmail.com
	> Created Time: 2013年04月18日 星期四 13时59分16秒
 ************************************************************************/

#include<stdio.h>
void swap(int x, int y)
{
	int temp;
	temp = x;
	x = y;
	y = temp;
}

int main(void)
{
	int x = 1;
	int y = 2;
	swap(x, y);
	printf("x=%d\ny=%d\n", x, y);
	return 0;
}
