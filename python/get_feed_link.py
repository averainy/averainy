#!/usr/bin/env python
#coding=utf-8
import feedparser
class getFeedLink:
	def __init__(self,feed):
		try:
			self.d=feedparser.parse(feed)
			self.status=True
		except:
			print u'解析feed失败，请检测网络和feed链接'
			self.status=False
		self.links=[]
	def Links(self):
		for l in self.d.entries:
			if l.link not in self.links:
				self.links.append(l.link)

if __name__ == '__main__':
	feed=getFeedLink('feed url')
	if feed.status is False:
		print 'lllll'
		exit(-1)
	feed.Links()
	print feed.links
