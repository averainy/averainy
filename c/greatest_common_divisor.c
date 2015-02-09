/*************************************************************************
	> File Name: greatest_common_divisor.c
	> Author: averainy
	> Mail: zhangyongxin@averainy.info
	> Created Time: 2013年04月16日 星期二 21时25分19秒
 ************************************************************************/

#include<stdio.h>
#include <stdlib.h>
/*求最大公约数
 * 使用Euclid算法：
 *
 * 如果a除以b能整除，则最大公约数是b。
 *
 * 否则，最大公约数等于b和a%b的最大公约数。
 */
int gcd(int n, int m)
{
	int temp;
	if (n < m) {
		temp = m;
		m = n;
		n = temp;
	}
	if (n % m == 0)
		return m;
	else {
		return gcd(n % m, m);
	}
}

int main(int argc, char *argv[])
{
	if (argc != 3) {
		printf("Usage:./a.out n,m");
		return -1;
	}
	int n = atoi(argv[1]);
	int m = atoi(argv[2]);
	printf("the result is %d\n", gcd(n, m));
	return 0;
}
