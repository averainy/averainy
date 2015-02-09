/*************************************************************************
  > File Name: count_number.c
  > Author: averainy
  > Mail: averainy@gmail.com
  > Created Time: 2013年04月18日 星期四 11时19分08秒
 ************************************************************************/

#include<stdio.h>
#include <stdlib.h>
#define N 20
/*
 * 统计20个0-9的随机数，同时打印直方图
 */
int a[N];

void gen_random(int upper_bound)
{
	int i;
	for (i = 0; i < N; i++)
		a[i] = rand() % upper_bound;
}

int howmany(int value)
{
	int count = 0, i;
	for (i = 0; i < N; i++)
		if (a[i] == value)
			++count;
	return count;
}

int main(void)
{
	int i, j, histogram[10] = { 0 }, big_number;
	srand(time(NULL));
	gen_random(10);
	for (i = 0; i < N; i++) {
		histogram[a[i]]++;
	}
	for (i = 0, big_number = histogram[0]; i < 10; i++) {
		printf("%d\t", i);
		if (big_number < histogram[i])
			big_number = histogram[i];

	}
	printf("\n");
	for (j = 0; j < big_number; j++) {
		for (i = 0; i < 10; i++) {
			if (histogram[i] > 0) {
				printf("*\t");
				histogram[i]--;
			} else
				printf(" \t");
		}

		printf("\n");
	}

	return 0;
}
