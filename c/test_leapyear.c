#include <stdio.h>
/*
 * 测试闰年函数，学习c语言应该都做过
int leap_year(int year)
{
    if(year%100==0){
        if(year%400==0)
            return 0;
    }
    else if(year%4==0)
        return 0;
    return -1;
}
int main(int argc,char *argv[])
{
    int year;
    year=atoi(argv[1]);
    if(leap_year(year)==0)
        printf("这是闰年\n");
    else
        printf("这不是闰年\n");
}
 
