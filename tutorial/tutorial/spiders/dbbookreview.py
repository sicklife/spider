# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DbbookItem
import os
from bs4 import BeautifulSoup
from scrapy.http.request import Request
from scrapy.extensions.closespider import CloseSpider


print (os.getcwd())

with open('counter.txt', 'r') as f:
    page = int(f.read().strip())


class DbbookreviewSpider(scrapy.Spider):
    global page
    name = "dbbookreview"
    handle_httpstatus_list = [404]
    allowed_domains = ["book.douban.com"]
    start_urls = ['http://book.douban.com/review/%s/' % page]
    #原来上一行少了一个/结果会多跳转一次，加上之后，就好了。下同

    def parse(self, response):
        """
        :param response:
        :return:
        这里的逻辑是，从start_urls调用地址，被内置的`make_request_from_url`函数调用，生成response，如果response
        没有被跳转到影评（`'book' in response.url`）或没有被删除，则爬取，并检验下一条。如果跳转或删除了，则检验下一条
        """
        global page
        print(response.url)
        if 'book' in response.url and response.status != 404:   #判断是否有跳转或404
            yield self.parse_item(response)
            page += 1
            yield Request('http://book.douban.com/review/%s/' % page, callback=self.parse)
            #parse下一个
        else:
            print("shit")
            page += 1
            yield Request('http://book.douban.com/review/%s/' % page, callback=self.parse)

    def parse_item(self, response):
        global page
        with open('counter.txt', 'w') as f:
            f.write(str(page))
        i = DbbookItem()
        soup = BeautifulSoup(response.body, "lxml")
        i['title'] = soup.h1.get_text()
        i['content'] = soup.find_all("span", property="v:description")[0].get_text()
        i['book'] = soup.find_all("span", property="v:itemreviewed")[0].get_text()
        i['author'] = soup.find_all("span", property="v:reviewer")[0].get_text()
        i['author_link'] = soup.find_all("span", class_="pl2")[0].a.get('href')
        i['book_link'] = soup.find_all("span", class_="pl2")[0].a.find_next('a').get('href')
        #print(i['title'])
        return i

        # 爬取下一个
