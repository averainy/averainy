/*
 * 通过 /dev/rtc (real-time clock) 硬件时钟实现的 timer机制。
 * 其中 ioctl(fd, RTC_IRQP_SET, 4) 的第三个参数只能是 2, 4, 8, 16, 32 之一，表示 xx Hz。
 */
#include <linux/rtc.h>
#include <sys/ioctl.h>
#include <sys/time.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <time.h>
#include <err.h>

int main(void)
{
	unsigned long i = 0;
	unsigned long data = 0;
	int fd = open("/dev/rtc", O_RDONLY);

	if (fd < 0)
		errx(1, "open() fail");

	/* set the freq as 4Hz */
	if (ioctl(fd, RTC_IRQP_SET, 4) < 0)
		errx(1, "ioctl(RTC_IRQP_SET) fail");

	/* enable periodic interrupts */
	if (ioctl(fd, RTC_PIE_ON, 0) < 0)
		errx(1, "ioctl(RTC_PIE_ON)");

	for (i = 0; i < 100; i++) {
		if (read(fd, &data, sizeof(data)) < 0)
			errx(1, "read() error");

		printf("timer %d\n", time(NULL));
	}

	/* enable periodic interrupts */
	if (ioctl(fd, RTC_PIE_OFF, 0) < 0)
		errx(1, "ioctl(RTC_PIE_OFF)");


	close(fd);
	return 0;
}
