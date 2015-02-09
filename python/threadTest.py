#!/usr/bin/env python
#coding=utf-8
import thread,time
count = 0
lock = thread.allocate_lock()
def threadTest():
	global count,lock
	lock.acquire()

	for i in xrange(10000):
		count += 1
	lock.release()
	print 'kk'
	time.sleep(6)
	print 'over'
for i in xrange(10):
	thread.start_new_thread(threadTest,())
time.sleep(10)
print count
