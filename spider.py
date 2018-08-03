# coding: utf-8
from  parseHtml import  HtmlParser
from Downloader import Downloader, UrlManager
from threadpool import  ThreadPool, makeRequests

class Spider(object):
    def __init__(self, startUrl, maxDepth = 3, threads = 10):
        self.startUrl = startUrl
        self.maxDepth = maxDepth
        self.threads = threads
        self.urlManager = UrlManager()
        self.urlManager.add_new_url(self.startUrl)
        self.threadpool = ThreadPool(threads)

    def runThread(self, curUrl):
        if not curUrl:
            return
        downloader = Downloader(curUrl)
        html = downloader.download()
        if html.code != 200:
            return
        parser = HtmlParser(curUrl, html)
        allHref = parser.get_a_href()
        if len(allHref) == 0:
            return
        for href in allHref:
            if 'http://' in href or 'https://' in href:
                print  href
                self.urlManager.add_new_url(href)

    def spider(self):
        curDepth = 0
        while curDepth < self.maxDepth and self.urlManager.has_new_url():
            while self.urlManager.has_new_url():
                requests = makeRequests(self.runThread, self.urlManager.get_all_urls())
                [self.threadpool.putRequest(req) for req in requests]
                self.threadpool.wait()
            curDepth += 1

if __name__ == '__main__':
    startUrl = 'https://www.cnblogs.com'
    myspider= Spider(startUrl)
    myspider.spider()
