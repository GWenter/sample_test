#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : LXH_content.py
# @Date    :2022/1/14 : 16:38
import csv
import json
import time

import requests as req


class Lxh(object):
    next = -1

    def __init__(self):
        self.url = 'https://api.bilibili.com/pgc/review/long/list?media_id=28221675&ps=20&sort=0&cursor={}'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'

        }

    def crawl(self):
        resp = req.get(self.url.format(self.next), headers=self.headers)
        html = resp.content.decode('utf-8')
        return html

    def parse(self, html):
        json_lxh = json.loads(html)
        self.next = json_lxh['data']['next']
        if self.next == 0:
            raise Exception('no data')
        list_ = []
        list_lxh = json_lxh['data']['list']
        for i in list_lxh:
            article_id = i['article_id']
            cmt = i['content']
            title = i['title']
            score = i['score'] / 2
            list_.append([article_id, title, score, cmt])
        return list_

    def save_csv(self, list_):
        with open(r'../data/lxh_content.csv', 'a', encoding='utf-8') as fd:
            writer = csv.writer(fd)
            writer.writerows(list_)


def init_csv():
    list_ = [['文章id', '标题', '评分', '', '内容']]
    with open(r'../data/lxh_content.csv', 'w', encoding='utf-8') as fd:
        writer = csv.writer(fd)
        writer.writerows(list_)


def main():
    lxh = Lxh()
    while True:
        try:
            content = lxh.crawl()
            list_ = lxh.parse(content)
            lxh.save_csv(list_)
            print('====have done ===')
            time.sleep(1)
        except Exception as ex:
            print("Spider error:" + str(ex))
            break


if __name__ == '__main__':
    init_csv()
    main()
