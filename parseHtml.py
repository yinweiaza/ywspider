# coding: utf-8
from bs4 import BeautifulSoup as bs
import lxml

class  HtmlParser(object):
    def __init__(self, host, html):
        self.html = html
        self.host = host

    def get_a_href(self):
        if not self.html:
            print('no html context')
            return
        soup = bs(self.html, 'lxml')
        aTags = soup.find_all('a')
        hrefs = set()
        for aCtx in aTags:
            if 'href' in aCtx.attrs:
                hrefs.add(aCtx['href'])
        return hrefs

