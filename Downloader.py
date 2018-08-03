# coding: utf-8

import  urllib
import urllib2
import config
import random

"""
    urls管理器；
"""
class  UrlManager(object):
    def __init__(self):
        self.newUrls = []
        self.oldUrls =  []

    def add_new_url(self, url):
        """
        添加一个网址；
        :param url:
        :return:
        """
        if url in self.newUrls or url in self.oldUrls:
            return
        self.newUrls.append(url)

    def add_new_urls(self, urls):
        """
        批量添加网址；
        :param urls:
        :return:
        """
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        """
        判断是否有新网址；
        :return:
        """
        return len(self.newUrls)

    def get_new_url(self):
        """
        返回一个新网络地址；
        :return:
        """
        try:
            url = self.newUrls.pop()
        except:
            print('null urls')
            return []
        if url:
            self.oldUrls.append(url)
            return url

    def  get_all_urls(self):
        urls = set()
        while self.has_new_url():
            curUrl = self.get_new_url()
            urls.add(curUrl)
        return urls

"""
    网页下载器；
"""
class Downloader(object):
    def __init__(self, url):
        self.url = url

    def get_random_headers(self):
        """
        获取随机请求头；
        :return:
        """
        return {'User-Agent': random.choice(config.user_agent)}

    def download(self):
        """
        下载网页；
        :return:
        """
        request = urllib2.Request(self.url, headers=self.get_random_headers())
        return urllib2.urlopen(request)
