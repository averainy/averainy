/*************************************************************************
	> File Name: full_permutation.c
	> Author: averainy
	> Mail: averainy@gmail.com
	> Created Time: 2013年04月18日 星期四 12时04分50秒
 ************************************************************************/
#include<stdio.h>
#include <stdlib.h>
#include<math.h>
#define SWAP(x,y,t) ((t)=(x),(x)=(y),(y)=(t))
#define MAX_SIZE101
void swap(int x, int y)
{
	int temp;
	temp = x;
	x = y;
	y = temp;
}

void perm(int[], int, int);
int main()
{
	int i, n;
	int list[MAX_SIZE];
	printf("Please enter a number:");
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		list[i] = i;
		// list[i]=rand()%n;
		printf("%d ", list[i]);
	}
	printf("\n");
	perm(list, 0, n - 1);
	return 0;
}

void perm(int list[], int i, int n)
{
	int j, temp;
	if (i == n) {
		for (j = 0; j <= n; j++) {
			printf("%d ", list[j]);
		}
		printf("\n");
	} else {
		for (j = i; j <= n; j++) {
			SWAP(list[i], list[j], temp);
			perm(list, i + 1, n);
			SWAP(list[i], list[j], temp);
		}
	}
}
