/*************************************************************************
	> File Name: factorial.c
	> Author: averainy
	> Mail: zhangyongxin@averainy.info
	> Created Time: 2013年04月16日 星期二 21时10分24秒
 ************************************************************************/

#include<stdio.h>
#include <stdlib.h>
int factorial(int n)
	/*这个函数是计算Ｎ的阶乘 */
{
	if (n == 0)
		return 1;
	else {
		int recurse = factorial(n - 1);
		int result = recurse * n;
		return result;
	}
}

int main(int argc, char *argv[])
{
	if (argc != 2) {
		printf("usage:./a.out number\n");
		return -1;
	}
	int number = atoi(argv[1]);
	printf("the result is %d\n", factorial(number));
	return 0;
}
