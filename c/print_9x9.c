/*************************************************************************
	> File Name: 9x9.c
	> Author: averainy
	> Mail: averainy@gmail.com
	> Created Time: 2013年04月17日 星期三 15时12分31秒
 ************************************************************************/

#include<stdio.h>
/* 打印9x9乘法表
 */
int print_9x9(void)
{
	int i, j;
	for (i = 1; i <= 9; i++) {
		for (j = 1; j <= i; j++)
			printf("%d\t", i * j);
		printf("\n");
	}
	return 0;
}

void main(void)
{
	print_9x9();
}
