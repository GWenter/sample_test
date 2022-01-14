#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : cjh.py
# @Date    :2022/1/14 : 10:37

# 1. pa

import csv
import re

import requests as req
from lxml import etree


class CJHSpider(object):
    path_csv = '../data/cjh.csv'
    start = 0

    def __init__(self):
        self.url = 'https://movie.douban.com/subject/25845392/comments?start={}&limit={}&status=P&sort=new_score'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Cookie': 'bid=fXONKxg4Sqg; ll="118254"; __gads=ID=62b5db7fe72b1bda-22c43698e6cf0064:T=1642127903:RT=1642127903:S=ALNI_MYbayxGa8Q7_NhApfaBNOysQenYFA; _vwo_uuid_v2=D9F2A74ABAF1CDA5F97FF5844A525AC93|b2ecf26b034d8e39dc1b31339d4fd634; __yadk_uid=3XK9jEJeSxwp1ojcXPABzu8AApAxTarA; ap_v=0,6.0; __utma=30149280.1278942737.1642127891.1642139071.1642141513.4; __utmc=30149280; __utmz=30149280.1642141513.4.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1642141520%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E9%2595%25BF%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.1703709027.1642127891.1642139071.1642141520.4; __utmb=223695111.0.10.1642141520; __utmc=223695111; __utmz=223695111.1642141520.4.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmb=30149280.9.10.1642141513; _pk_id.100001.4cf6=361fc9bff3090018.1642127891.4.1642143256.1642139066.'
        }

    def crawl(self, limit):
        resp = req.get(self.url.format(self.start, limit), headers=self.headers)
        self.start += limit
        # print(type(resp))
        html = resp.content.decode('utf-8')
        # print(html)
        return html

    def parse(self, html):
        """"""
        root = etree.HTML(html)
        comments = root.xpath('//*[@id="comments"]/div[@data-cid]')
        if len(comments) <= 0:
            raise Exception('no data')
        # print(comments)
        movies = []
        for c in comments:
            name = c.xpath("./div[2]/h3/span[2]/a/text()")[0].strip()  # 姓名
            looked = c.xpath("./div[2]/h3/span[2]/span[1]/text()")[0].strip()  # 是否看过
            stars = c.xpath("./div[2]/h3/span[2]/span[2]/@class")[0].strip()
            stars = re.sub(r'\D', '', stars)  # 星级
            hot = c.xpath("./div[2]/h3/span[1]/span/text()")[0].strip()  # 热度
            cmt = c.xpath("./div[2]/p/span/text()")[0].strip()  # 评论
            movies.append([name, looked, stars, hot, cmt])
        return movies

    def save_csv(self, list_movies):
        with open(r'../data/cjh.csv', 'a', encoding='utf-8') as fd:
            writer = csv.writer(fd)
            writer.writerows(list_movies)


def main():
    cjh_spider = CJHSpider()
    try:
        while True:
            content = cjh_spider.crawl(1000)
            movies = cjh_spider.parse(content)
            cjh_spider.save_csv(movies)
            print("====")
    except Exception as ex:
        print("Spider error:" + str(ex))


if __name__ == '__main__':
    main()
