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

    def __init__(self):
        self.url = 'https://movie.douban.com/subject/25845392/comments?start=0&limit=100&status=P&sort=new_score'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'

        }

    def crawl(self):
        resp = req.get(self.url, headers=self.headers)
        # print(type(resp))
        html = resp.content.decode('utf-8')
        # print(html)
        return html

    def parse(self, html):
        """"""
        root = etree.HTML(html)
        comments = root.xpath('//*[@id="comments"]/div[@data-cid]')
        # print(comments)
        movies = [['姓名', '是否看过', '星级', '热度', '时间', '评论']]
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
    content = cjh_spider.crawl()
    movies = cjh_spider.parse(content)
    cjh_spider.save_csv(movies)


if __name__ == '__main__':
    main()
