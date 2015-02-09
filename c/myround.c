#include <stdio.h>
#include <stdlib.h>
#include <math.h>
double myround(double x)
	/*实现x四舍五入
	 */
{
	if ((ceil(x) - x) > 0.5)
		return floor(x);
	else
		return ceil(x);
}

int main(int argc, char *argv[])
{
	double number;
	number = atof(argv[1]);
	printf("number is %f\n", number);
	printf("myround result is %f\n", myround(number));
	return 0;
}
