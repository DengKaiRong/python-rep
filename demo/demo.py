# coding=utf-8

import time

def printTimeAndSleep(sec,String):
	print String
	while 1:
		now = time.time()
		localTime = time.localtime(now)
		dateStr = time.strftime('%Y-%m-%d %H:%M:%S',localTime)
		print '现在时间: ' + dateStr
		time.sleep(sec)
	return

printTimeAndSleep(1,'邓小帅时钟')