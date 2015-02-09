/*************************************************************************
	> File Name: number.c
	> Author: averainy
	> Mail: averainy@gmail.com
	> Created Time: 2013年04月17日 星期三 13时45分07秒
 ************************************************************************/

#include<stdio.h>
#include <stdlib.h>
/*
 * check_number这个函数计算number中含有几个n
 */
int check_number(int number, int n)
{
	int m;
	int i = 0;
	do {
		m = number % 10;
		if (m == 9)
			i++;
	} while (number /= 10);
	return i;
}

int main(int argc, char *argv[])
{
	int n = atoi(argv[1]), i = 0;
	while (n) {
		i += check_number(n, 9);
		n--;
	}
	printf("there are %d 9 beetwin 1 and  %s\n", i, argv[1]);
	return 0;
}
