#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : top_250.py
# @Date    :2022/1/14 : 19:24

import csv
import time

import requests as req
from lxml import etree


class Top(object):
    start = 0

    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start={}&filter='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Cookie': 'bid=fXONKxg4Sqg; ll="118254"; __gads=ID=62b5db7fe72b1bda-22c43698e6cf0064:T=1642127903:RT=1642127903:S=ALNI_MYbayxGa8Q7_NhApfaBNOysQenYFA; _vwo_uuid_v2=D9F2A74ABAF1CDA5F97FF5844A525AC93|b2ecf26b034d8e39dc1b31339d4fd634; __yadk_uid=3XK9jEJeSxwp1ojcXPABzu8AApAxTarA; __utmc=30149280; __utmz=30149280.1642159334.5.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; __utmc=223695111; __utmz=223695111.1642159361.5.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.1278942737.1642127891.1642159334.1642163132.6; __utmb=30149280.0.10.1642163132; __utma=223695111.1703709027.1642127891.1642159361.1642163132.6; __utmb=223695111.0.10.1642163132; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1642163132%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ct=y; _pk_id.100001.4cf6=361fc9bff3090018.1642127891.6.1642164949.1642159471.'

        }

    def crawl(self):
        resq = req.get(self.url.format(self.start), headers=self.headers)
        self.start += 25
        html = resq.content.decode('utf-8')
        return html

    def parse(self, html):
        root = etree.HTML(html)
        comments = root.xpath('//div[@class="item"]')
        # print(type(comments))     # list
        if len(comments) <= 0:
            raise Exception("no data")
        movies = []
        for m in comments:
            rank = m.xpath("./div[1]/em/text()")[0].strip()
            name = m.xpath('./div[2]/div[1]/a/span[1]/text()')[0].strip()
            cmt = m.xpath('./div[2]/div[2]/div/span[2]/text()')[0].strip()
            peo = m.xpath('./div[2]/div[2]/div/span[4]/text()')[0].strip()
            tip = m.xpath('./div[2]/div[2]/p[2]/span/text()')[0].strip()
            movies.append([rank, name, cmt, peo, tip])
        return movies

    def save_csv(self, list_movies):
        with open(r'../data/top_250.csv', 'a', encoding='utf-8') as fd:
            writer = csv.writer(fd)
            writer.writerows(list_movies)


def init_csv():
    list_ = [['排名', '电影名称', '评分', '评论人数', '书签']]
    with open(r'../data/top_250.csv', 'w', encoding='utf-8') as fd:
        writer = csv.writer(fd)
        writer.writerows(list_)


def main():
    top = Top()
    while True:
        try:
            html = top.crawl()
            movies = top.parse(html)
            top.save_csv(movies)
            print('===have done===')
            time.sleep(1)
        except Exception as ex:
            print("Spider error: " + str(ex))
            break


if __name__ == "__main__":
    init_csv()
    main()
