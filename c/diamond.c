/*************************************************************************
	> File Name: diamond.c
	> Author: averainy
	> Mail: averainy@gmail.com
	> Created Time: 2013年04月17日 星期三 15时19分43秒
 ************************************************************************/

#include<stdio.h>
#include <math.h>
/*
 * 打印菱形图案
 */
int diamond(int n, char c)
{
	if (n % 2 == 0) {
		printf("error 参数不能为偶数\n");
		return -1;
	}
	int i, j, k, m;
	for (i = 1; i < n; i += 2) {
		for (k = 0; k < (n - i) / 2; k++)
			printf(" \t");
		for (k = 0; k < i; k++)
			printf("%c\t", c);
		printf("\n");
	}
	for (i = n; i > 0; i -= 2) {
		for (k = 0; k < (n - i) / 2; k++)
			printf(" \t");
		for (k = 0; k < i; k++)
			printf("%c\t", c);
		printf("\n");
	}
}

void main(void)
{
	diamond(9, '*');
}
