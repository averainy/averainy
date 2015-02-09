/*
 * 功能: 简单操作，打开/dev/rtc， 然后获取 时间信息
 * ioctl 命令
 * #define RTC_AIE_ON   打开alarm中断
 * #define RTC_AIE_OFF   关闭 alarm中断
 * #define RTC_UIE_ON    打开update类型的中断
 * #define RTC_UIE_OFF   关闭
 * #define RTC_PIE_ON    打开周期性中断
 * #define RTC_PIE_OFF   关闭
 * #define RTC_WIE_ON    
 * #define RTC_WIE_OFF
 *
 * #define RTC_ALM_SET     设置alarm的时间
 * #define RTC_ALM_READ     读取alarm的时间
 * #define RTC_RD_TIME   读取当前的rtc时间
 * #define RTC_SET_TIME   设置当前的rtc时间
 * #define RTC_IRQP_READ  读取当前周期性中断的频率
 * #define RTC_IRQP_SET   设置当前周期性中断的频率
 * #define RTC_EPOCH_READ
 * struct rtc_time {
 *     int tm_sec;
 *     int tm_min;
 *     int tm_hour;
 *     int tm_mday;
 *     int tm_mon;
 *     int tm_year;
 *     int tm_wday;
 *     int tm_yday;
 *     int tm_isdst;
 *     };
 */
#include <stdio.h>		//printf funciton
#include <stdlib.h>		//EXIT_FAILURE
#include <linux/rtc.h>		//usr/include/linux/rtc.h struct rtc_time
#include <fcntl.h>		//O_RDONLY open close funciton
#include <sys/ioctl.h>		//ioctl funciton /usr/include/sys/ioctl

int main(int argc, char *argv[])
{
	int retval, fd;
	struct rtc_time rtc_tm;

	fd = open("/dev/rtc", O_RDONLY);
	if (fd == -1) {
		perror("error open /dev/rtc");
		exit(EXIT_FAILURE);
	}

	retval = ioctl(fd, RTC_RD_TIME, &rtc_tm);
	if (retval == -1) {
		perror("error RTC_RD_TIME ioctl");
		exit(EXIT_FAILURE);
	}
	printf("sec=%d,min=%d,hour=%d\n", rtc_tm.tm_sec, rtc_tm.tm_min,
	       rtc_tm.tm_hour);

	close(fd);

	exit(EXIT_SUCCESS);

}
