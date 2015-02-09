/*************************************************************************
	> File Name: is_prime.c
	> Author: averainy
	> Mail: averainy@gmail.com
	> Created Time: 2013年04月17日 星期三 14时43分42秒
 ************************************************************************/

#include<stdio.h>
/*
 * 这个是一个判断给定的n是否是素数的代码
 */
int is_prime(int n)
{
	int i;
	for (i = 2; i < n; i++)
		if (n % i == 0)
			break;
	if (i == n)
		return 1;
	else
		return 0;
}

int main(void)
{
	int i;
	for (i = 1; i <= 100; i++) {
		if (!is_prime(i))
			continue;
		printf("%d\n", i);
	}
	return 0;
}
